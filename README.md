# Genshin Impact Code Redeemer
![Screenshot 2024-09-27 at 11 10 28 PM](https://github.com/user-attachments/assets/58c06428-c57d-498e-90b7-4541167e56f2)

## Description
This is an automated script designed to scrape redeem codes for Genshin Impact from the internet and redeem them directly into player accounts. The script retrieves the latest codes from a specified website and uses user credentials to log in and redeem the codes.

## Features
- Scrapes the latest Genshin Impact redeem codes from [Pocket Tactics](https://www.pockettactics.com/genshin-impact/codes).
- Automatically logs into user accounts using credentials stored in a JSON file.
- Redeems codes with a specified delay to avoid rate-limiting.
- User-friendly output indicating the status of each redemption attempt.

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using:
```bash
pip install requests beautifulsoup4
```

## How to Use

## 1. Set Up Credentials

Before you begin, you'll need to retrieve your account credentials and x-rpc-app_id from the network inspection, as all account and password information is encrypted by Mihoyo. Create a `credentials.json` file in the same directory as the script. The file should follow this structure:

```json
{
    "username1": {
        "account": "your_account",
        "password": "your_password",
        "x-rpc-app_id": "your_x-rpc-app_id",
        "x-rpc-game_biz": "your_x-rpc-game_biz",
        "region": "your_region",
        "uid": "your_uid",
        "token_type": 4
    },
    "username2": {
        "account": "another_account",
        "password": "another_password",
        "x-rpc-app_id": "your_x-rpc-app_id",
        "x-rpc-game_biz": "your_x-rpc-game_biz",
        "region": "your_region",
        "uid": "another_uid",
        "token_type": 4
    }
}
```
### Region list:
```json
{
        "America": "os_usa",
        "Europe": "os_euro",
        "Asia": "os_asia",
        "TW,HK,MO": "os_cht"
}
```

## Accessing Encrypted Account Credentials

All account and password information is encrypted by Mihoyo. To retrieve the encoded values, please use the following steps in Google Chrome.

### Step 1:
Navigate to the [Genshin Impact Gift Page](https://genshin.hoyoverse.com/en/gift).

### Step 2:
Open the Developer Tools in Chrome and select the **Network** tab.
[Google: Inspect network activity](https://developer.chrome.com/docs/devtools/network)
### Step 3:
Log in to your account.

### Step 4:
In the **Network** tab:
- Copy the account and password from the payload of the `webLoginByPassword` request.
- Copy the `x-rpc-app_id` and `x-rpc-game_biz` from the **Headers** section under **Request Headers** of the `webLoginByPassword` request.


### 2. Configure the Script:

Open the script and adjust the `TARGET_USER` variable to the username you want to use for redeeming codes.
For example: TARGET_USER = "your_username"

### 3. Run the Script:

Open your terminal, navigate to the directory where the script is located, and execute:
```bash
python main.py
```
### 4. Testing result with used codes (5.1 liveStream Codes):

```bash
Extracted Codes:
XSME6NV4GX2Z
KALF66CLGXKM
PT5WP6D5GXJ9
------------Got Redeem codes------------
------------Got User------------
<username>
{"data":null,"message":"This Redemption Code is already in use","retcode":-2017}
{"data":null,"message":"This Redemption Code is already in use","retcode":-2017}
{"data":null,"message":"This Redemption Code is already in use","retcode":-2017}
------------Succeed------------
```
## Have Fun !!


## License

This project is licensed under the [MIT License](LICENSE).
