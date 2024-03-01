#!/usr/bin/python3
"""script that takes in a URL , sends a request to the URL
displays the body of response"""
import urllib.request
import urllib.parse
import urllib.error
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
