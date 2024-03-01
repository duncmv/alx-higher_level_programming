#!/usr/bin/python3
"""cript that takes in a URL and an email, sends a  POST request to the URL
displays the body of response"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data).encode('utf-8')
    with urllib.request.urlopen(sys.argv[1], data=data) as resp:
        print(resp.read().decode('utf-8'))
