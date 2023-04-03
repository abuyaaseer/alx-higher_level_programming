#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as get:
        value = get.read()
        print("Body response:")
        print("\t- type: {}".format(type(value)))
        print("\t- content: {}".format(value))
        print("\t- utf8 content: {}".format(value.decode('utf-8')))
