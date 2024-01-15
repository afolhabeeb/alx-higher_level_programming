#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_mat = [[0] * len(matrix[0]) for _ in range(len(matrix))]

    for num in range(len(matrix)):
        for nums in range(len(matrix[0])):
            squared_mat[num][nums] = matrix [num][nums] ** 2
    return (squared_mat)
