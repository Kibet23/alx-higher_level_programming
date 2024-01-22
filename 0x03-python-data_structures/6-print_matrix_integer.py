#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for k, num in enumerate(row):
            print("{:d}".format(num), end="")
            if k < len(row) - 1:
                print(" ", end="")
        print()
