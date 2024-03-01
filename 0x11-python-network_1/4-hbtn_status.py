#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    with requests.get("https://alx-intranet.hbtn.io/status") as resp:
        print('Body response:')
        print(f'\t- type: {type(resp.text)}')
        print(f'\t- content: {resp.text}')
