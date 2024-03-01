#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}

    resp = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        data = resp.json()
        print(f"[{data.id}] {data.name}")
    except requests.exceptions.JSONDecodeError:
        if resp.status_code == 204:
            print('No result')
        else:
            print('Not a valid JSON')
