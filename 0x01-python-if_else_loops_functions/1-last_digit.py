#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digit = number % -10
else:
    digit = number % 10

if digit > 5:
    stat = "and is greater than 5"
elif digit == 0:
    stat = "and is 0"
else:
    stat = "and is less than 6 and not 0"

print(f"Last digit of {number:d} is {digit:d} {stat}")
