#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    d = a_dictionary.copy()
    d = {key: x * 2 for key, x in d.items()}
    return d
