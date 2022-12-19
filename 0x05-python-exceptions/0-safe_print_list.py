#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for idx, el in enumerate(my_list):
            if idx == x:
                break
            print("{}".format(el), end="")
            count += 1
    except IndexError:
        count = 5
    print()
    return count
