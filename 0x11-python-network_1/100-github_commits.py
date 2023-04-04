#!/usr/bin/python3
"""
interview prep
"""
import sys
import requests


if __name__ == "__main__":
    # Get the arguments, arg1: repo name, arg2: repo owner
    URL = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])

    a = requests.get(url)
    commits = a.json()
    try:
        for i in range(10):
            print(f"{commits[i]['sha']}: {commits[i]['commit']['author']['name']}")
    except IndexError:
        pass
