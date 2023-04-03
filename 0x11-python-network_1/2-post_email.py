#!/usr/bin/python3
"""
-Takes in a URL and email,
-send POST request,
-and displays body of response decoded in utf-8
"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    req = sys.argv[1]
    values = {"email": sys.argv[2]}
    ans = urllib.parse.urlencode(values).encode("ascii")

    request = urllib.request.Request(req, ans)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
