#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for inte in row:
            print("{:d}".format(inte), end="")
        print()
