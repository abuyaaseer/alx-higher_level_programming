#!/usr/bin/python3
"""
interview prep
"""
import sys
import requests


if __name__ == "__main__":
    info = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    a = requests.get(info)
    commits = a.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
