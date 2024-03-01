#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        info = resp.read()
        print('Body response:')
        print(f'\t- type: {type(info)}')
        print(f'\t- content: {info}')
        print('\t- utf8 content: OK')
