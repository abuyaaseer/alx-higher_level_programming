#!/usr/bin/python3
"""
-script that takes in a URL, sends a request to the URL
-and displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    g = sys.argv[1]
    a = requests.g(url)
    try:
        a.raise_for_status()
        print(a.text)
    except Exception as ex:
        print("Error code: {}".format(a.status_code))
