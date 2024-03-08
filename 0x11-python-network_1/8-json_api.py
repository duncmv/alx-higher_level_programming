#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        payload = {'q': sys.argv[1]}
    else:
        payload = {'q': ""}

    resp = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        data = resp.json()
        if data:
            print(f"[{data.get('id')}] {data.get('name')}")
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
