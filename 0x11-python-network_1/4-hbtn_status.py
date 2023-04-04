!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    g = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(g.text)))
    print("\t- content: {}".format(g.text))
