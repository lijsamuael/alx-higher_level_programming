#!/usr/bin/python3
def print_sorted_dictionary(d):
    for k, v in sorted(d.items()):
        print("{}: {}".format(k, v))
