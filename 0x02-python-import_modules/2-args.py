#!/usr/bin/python3
import sys
n = len(sys.argv)
if n == 2:
    print("{} argument:".format(n-1))
else:
    print("{} arguments:".format(n-1))
for x in range(1, n):
    print("{}: {}".format(x, sys.argv[x]))
