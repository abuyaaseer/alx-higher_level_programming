#!/usr/bin/python3
"""
-script that takes in a URL
-sends a request to the URL
-displays the body of the response
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    get = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(get) as a:
            print(a.read().decode('utf-8'))
    except urllib.error.URLError as b:
        print("Error code: {}".format(b.code))
