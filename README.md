# Genshin Impact Code Redeemer

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

