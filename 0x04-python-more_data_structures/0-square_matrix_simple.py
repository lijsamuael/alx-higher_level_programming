#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = list(map(list, matrix))
    new_mat = [[x ** 2 for x in i] for i in new_mat]

    return new_mat
