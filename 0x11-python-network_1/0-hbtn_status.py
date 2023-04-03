#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    with urlib.request.urlopen('https://intranet.hbtn.io/status') as get:
        value = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(value)))
        print("\t- content: {}".format(value))
        print("\t- utf8 content: {}".format(value.decode('utf-8')))
