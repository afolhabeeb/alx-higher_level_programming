#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for inte in row:
                print("{:d}".format(inte), end=' ' if inte != row[-1] else '')
            print()
