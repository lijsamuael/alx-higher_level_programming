#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_string = repr(number)
num_str = num_string[-1]
num_strg = int(num_str)
num_strg = num_strg + 0
less = "and is less than 6 and not 0"
if num_strg > 5:
    stat = "and is greater than 5"
elif num_strg == 0:
    stat = "and is 0"
else:
    stat = less

if number < 0:
    print(f"Last digit of {number:d} is -{num_strg:d} {less}")
else:
    print(f"Last digit of {number:d} is {num_strg:d} {stat}")
