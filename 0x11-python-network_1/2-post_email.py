#!/usr/bin/python3
"""cript that takes in a URL and an email, sends a  POST request to the URL
displays the body of response"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1], data=sys.argv[2]) as resp:
        print(resp.read())
