#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_mat = []

    for row in matrix:
        squared_row = [num**2 for num in row]
        squared_mat.append(squared_row)
    return (squared_mat)
