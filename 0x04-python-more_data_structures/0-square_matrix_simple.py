#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix
    Parametrs:
    A 2d list representing a matrix
    Return:
    A new matrix with the square values
    """
    up_matrix = [[y**2 for y in row] for row in matrix]
    return (up_matrix)
