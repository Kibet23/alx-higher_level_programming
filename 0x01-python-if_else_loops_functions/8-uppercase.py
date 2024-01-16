#!/usr/bin/python3

def uppercase(str):
    """
    prints the string s in uppercase

    Args:
    str: input string

    Returns:
        NULL
    """
    for char in str:
        if 'a' <= char <= 'z':
            upp_char = chr(ord(char) - ord('a') + ord('A'))
            print("{}".format(upp_char), end="")
        else:
            print("{}".format(char), end="")
    print() # print a new line at the end
