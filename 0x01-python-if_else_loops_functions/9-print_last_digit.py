#!/usr/bin/python3

def print_last_digit(number):
    """
    print the last digit of a given number

    Args:
        number: input number

    Return:
        NULL
    """
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
