#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for idx, el in enumerate(my_list):
            if x == idx:
                break
            print("{}".format(el), end="")
    except IndexError:
        pass
    return idx
