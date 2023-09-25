#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            b = b * b
            print (b)