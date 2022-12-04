#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) = 0:
        return None
    reversed_list = my_list[::-1]
    for i in reversed_list:
        print("{:d}".format(i))
