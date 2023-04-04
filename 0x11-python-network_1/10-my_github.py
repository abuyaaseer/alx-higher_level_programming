#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests


if __name__ == "__main__":
    inf = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    a = requests.get("https://api.github.com/user", inf=inf)
    print(a.json().get("id"))
