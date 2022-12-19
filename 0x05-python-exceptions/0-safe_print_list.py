#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for idx, el in enumerate(my_list):
        if x == idx:
            break
        print("{:d}".format(el), end="")
