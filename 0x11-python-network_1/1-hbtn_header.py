#!/usr/bin/python3
"""Take in a URL,
  -sends request to URL
  -and display value of `X-Request-Id`
"""

import sys
from urllib import request

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as get:
        print(get.info()['X-Request-Id'])
