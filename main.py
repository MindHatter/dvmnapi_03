import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def count_clicks(token, target_url):
    parsed_target_url = urlparse(target_url)
    bitly_api_url = "".join([
        "https://api-ssl.bitly.com/v4/bitlinks/",
        f"{parsed_target_url.netloc}/{parsed_target_url.path}",
        "/clicks/summary"
    ])

    headers = {
        "Authorization": token,
    }

    params = {
        "unit": "month",
    }

    response = requests.get(bitly_api_url, headers=headers, params=params)
    response.raise_for_status()
    clicks = response.json()["total_clicks"]

    return clicks


def shorten_link(token, target_url):
    bitly_api_url = "https://api-ssl.bitly.com/v4/bitlinks"

    headers = {
        "Authorization": token,
    }

    params = {
        "long_url": target_url,
    }

    response = requests.post(bitly_api_url, headers=headers, json=params)
    response.raise_for_status()
    link = response.json()["link"]

    return link


def is_bitlink(token, target_url):
    parsed_target_url = urlparse(target_url)
    bitly_api_url = "".join([
        "https://api-ssl.bitly.com/v4/bitlinks/",
        f"{parsed_target_url.netloc}/{parsed_target_url.path}",
    ])

    headers = {
        "Authorization": token,
    }

    response = requests.get(bitly_api_url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Enter URL for compress or bitlink")
    args = parser.parse_args()
    
    target_url = args.url
    parsed_target_url = urlparse(target_url)
    if not all([parsed_target_url.scheme, parsed_target_url.netloc]):
        raise ValueError("Your URL is not a valid URL")

    bitly_access_token = os.environ['BITLY_ACCESS_TOKEN']

    if not is_bitlink(bitly_access_token, target_url):
        bitly_link = " ".join([
            "Bitly link: ",
            shorten_link(bitly_access_token, target_url)
        ])
        print(bitly_link)
    else:
        bitly_link_clicks = " ".join([
            "Clicks: ",
            str(count_clicks(bitly_access_token, target_url))
        ])
        print(bitly_link_clicks)


if __name__ == "__main__":
    main()
