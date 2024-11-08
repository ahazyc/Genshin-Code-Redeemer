import requests
import json
import time
from bs4 import BeautifulSoup

# URL to scrape Genshin Impact codes from
Genshin_Codes_URL = "https://www.pockettactics.com/genshin-impact/codes"
# Thank you! pockettactics!
TIME_DELAY = 5.5  # Delay time between requests
# TARGET_USER can be set to a specific username
TARGET_USER = "username1"

def readCredentials():
    with open('credentials.json', 'r') as file:
        data = json.load(file)
    return data

def scrape_codes_from_first_ul(url):
    """Scrape redeem codes from the first <ul> tag found on the specified URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the <div class="entry-content"> and then the first <ul> tag within it
        entry_content = soup.find('div', class_='entry-content')

        if entry_content:
            first_ul = entry_content.find('ul')  # Get the first <ul> within this div

            if first_ul:
                codes = []
                # Extract codes from the <strong> <b> tags within <li> elements
                for li in first_ul.find_all('li'):
                    b_tag = li.find('b')
                    if b_tag:
                        codes.append(b_tag.get_text(strip=True))

                    strong_tag = li.find('strong')
                    if strong_tag:
                        codes.append(strong_tag.get_text(strip=True))

                # Print the extracted codes
                print("Extracted Codes:")
                for code in codes:
                    print(code)

                return codes
            else:
                print("No <ul> tag found within the entry-content div.")
        else:
            print("No <div class='entry-content'> found on the page.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def login(user):
    """Log in to the Hoyoverse account and return cookies."""
    url = "https://sg-public-api.hoyoverse.com/account/ma-passport/api/webLoginByPassword"

    account = user["account"]
    password = user["password"]
    x_rpc_app_id = user["x-rpc-app_id"]
    x_rpc_game_biz = user["x-rpc-game_biz"]

    payload = json.dumps({
        "account": account,
        "password": password,
        "token_type": 4
    })

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://account.hoyoverse.com',
        'Referer': 'https://account.hoyoverse.com/',
        'x-rpc-app_id': x_rpc_app_id,
        "x-rpc-game_biz": x_rpc_game_biz,
        "x-rpc-language": 'en'
    }

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        # Extract cookies from the Set-Cookie header
        cookie_header = response.headers.get('Set-Cookie', '')
        cookies = {}
        for cookie in cookie_header.split(', '):
            key, value = cookie.split(';')[0].split('=', 1)
            cookies[key] = value
        # print(cookies)  # Print cookies for debugging
        return cookies
    else:
        print("------------Login Failed------------")
        return None

def redeemCode(user, cdKey, cookies):
    uid = user["uid"]
    x_rpc_game_biz = user["x-rpc-game_biz"]
    uid = user["uid"]
    region = user["region"]
    """Redeem a code using the user's UID and the provided cookies."""
    # TODO: Ensure "hk4e" or other part of the URL is correct for users in different regions
    url = (
        f"https://sg-hk4e-api.hoyoverse.com/common/apicdkey/api/webExchangeCdkey"
        f"?uid={uid}&region={region}&lang=en&cdkey={cdKey}&game_biz={x_rpc_game_biz}&sLangKey=en-us"
    )

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'cache-control': 'no-cache',
        'origin': 'https://genshin.hoyoverse.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://genshin.hoyoverse.com/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers, cookies=cookies)

    print(response.text)

# Example usage
if __name__ == "__main__":
    codes = scrape_codes_from_first_ul(Genshin_Codes_URL)
    if len(codes) == 3:  # Ensure there are 3 codes
        print("------------Got Redeem codes------------")
        credentials = readCredentials()
        user = credentials.get(TARGET_USER)  # Use .get to avoid KeyError
        
        if user:
            print("------------Got User------------")
            print(TARGET_USER)
            cookies = login(user)
            if cookies:
                time.sleep(TIME_DELAY)
                for code in codes:
                    redeemCode(user, code, cookies)
                    time.sleep(TIME_DELAY)
                print("------------Succeed------------")
            else:
                print("------------Login failed, cannot redeem codes------------")
        else:
            print("------------Can't find user------------")
    else:
        print("------------Insufficient codes extracted------------")
