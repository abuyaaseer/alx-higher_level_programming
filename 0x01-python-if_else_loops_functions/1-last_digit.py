#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number >= 0):
    remainder = number % 10
if (number < 0):
    remainder = number % -10

print("Last digit of {} is {} and is".format(number, remainder), end="")
if (remainder > 5):
    print(" greater than 5")
elif (remainder == 0):
    print(" 0".format(number, remainder))
else:
    print(" less than 6 and not 0")
