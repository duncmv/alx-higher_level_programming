#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)
uses the GitHub API to display your id"""
import requests
import sys

if __name__ == "__main__":
    url = f'http://api.github.com/users/{sys.argv[1]}'
    head = {'Authorization': f'token {sys.argv[2]}'}
    resp = requests.get(url, headers=head)
    print(resp.json().get('id'))
