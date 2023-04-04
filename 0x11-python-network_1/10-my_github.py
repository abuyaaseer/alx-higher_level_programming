#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])

    a = requests.get(url)
    commits = a.json()
    try:
        for i in range(10):
            print(f"{commits[i]['sha']}: {commits[i]['commit']['author']['name']}")
    except IndexError:
        pass
