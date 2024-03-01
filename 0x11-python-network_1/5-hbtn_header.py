#!/usr/bin/python3
"""cript that takes in a URL, sends a request to the URL
displays the value of the X-Request-Id variable"""
import requests
import sys


if __name__ == "__main__":
    resp = requests.get(sys.argv[1])
    print(resp.headers['X-Request-Id'])
