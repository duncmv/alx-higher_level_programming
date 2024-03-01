#!/usr/bin/python3
"""script that takes in a URL , sends a request to the URL
displays the http code"""
import requests
import sys


if __name__ == "__main__":
    with requests.get(sys.argv[1]) as resp:
        if resp.status_code >= 400:
            print('Error code:', resp.status_code)
        else:
            print(resp.text)
