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
        print("{}".format(chr(ord(char) - 32)
                          if 'a' <= char <= 'z' else char), end="")
    print()  # print a new line at the end
