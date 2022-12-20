#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tbd = []
    for k, v in a_dictionary.items():
        if v == value:
            tbd.append(k)

    for i in tbd:
        del a_dictionary[i]

    return a_dictionary
