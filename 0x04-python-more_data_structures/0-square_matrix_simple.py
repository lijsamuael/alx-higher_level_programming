#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for i in range(3):
        for j in range(3):
            new_m[i][j] = matrix[i][j] * matrix[i][j]
    return new_m
