#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)
uses the GitHub API to display your id"""
import requests
import sys

if __name__ == "__main__":
    url = f'http://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'
    resp = requests.get(url)
    commits = resp.json()
    for i in range(10):
        if i < len(commits):
            com = commits[i]
            print(f'{com["sha"]}: {com["commit"]["author"]["name"]}')
