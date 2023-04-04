#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user 
with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        arg = ""
    payload = {'q': arg}
    URL = "http://0.0.0.0:5000/search_user"
    a = requests.post(URL, data=payload)
    try:
        a.raise_for_status()
        js = a.json()
        if len(js) == 0:
            print("No result")
        else:
            print("[{:d}] {}".format(js['id'], js['name']))
    except Exception:
        print("Not a valid JSON")
