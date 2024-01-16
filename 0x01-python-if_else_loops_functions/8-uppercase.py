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
        if 'a' <= char <= 'z':
            upp_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            upp_char = char

        result += "{}".format(upp_char)

    print(result)
