#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == '__main__':
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] not in "-+*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    opp = sys.argv[2]
    if opp == '+':
        print('{} + {} = {}'.format(a, b, add(a, b)))
    if opp == '-':
        print('{} - {} = {}'.format(a, b, sub(a, b)))
    if opp == '*':
        print('{} * {} = {}'.format(a, b, mul(a, b)))
    if opp == '/':
        print('{} / {} = {}'.format(a, b, div(a, b)))
