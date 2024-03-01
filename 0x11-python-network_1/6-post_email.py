#!/usr/bin/python3
"""script that takes in a URL and an email, sends a  POST request to the URL
displays the body of response"""
import requests
import sys


if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    with requests.post(sys.argv[1], data=data) as resp:
        print(resp.text)
