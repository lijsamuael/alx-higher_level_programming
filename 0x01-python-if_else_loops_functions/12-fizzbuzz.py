#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if (not (x % 5 == 0 or x % 3 == 0)):
            print("{}".format(x), end=" ")
        elif (x % 5 == 0 and x % 3 == 0):
            print("FizzBuzz", end=" ")
        elif (x % 5 == 0):
            print("Buzz", end=" ")
        else:
            print("Fizz", end=" ")
