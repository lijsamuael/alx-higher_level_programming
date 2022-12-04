#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum_first = 0
    sum_second = 0
    for i in range(2):
        if i == 0:
            if i < len(tuple_a):
                sum_first += tuple_a[i]
            if i < len(tuple_b):
                sum_first += tuple_b[i]
        if i == 1:
            if i < len(tuple_a):
                sum_second += tuple_a[i]
            if i < len(tuple_b):
                sum_second += tuple_b[i]
    return (sum_first, sum_second)
