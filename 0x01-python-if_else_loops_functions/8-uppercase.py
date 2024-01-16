#!/usr/bin/python3

def uppercase(str):
    """
    prints the string s in uppercase

    Args:
    str: input string

    Returns:
        NULL
    """
    result = ""
    for char in str:
        result += "{}".format(chr(ord(char) - 32) if 'a' <= char <= 'z' else
                              char)
    print(result)  # print a new line at the end
