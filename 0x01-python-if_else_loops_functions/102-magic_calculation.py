#!/usr/bin/python3
def magic_calculation(a, b, c):
    """
    magic_calculation - does the magic calculation
    Args:
        a - first integer
        b - second integer
        c - third integer
    Return:
        the value after the magic calculation
    """
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c
