#!/usr/bin/python3
def remove_char_at(str, n):
    """
    creates a copy of the string, removing the character at the postion n
    Args:
        str: string
        n: position

    Return: modified string
    """
    if n < 0 or n >= len(str):
        return str

    return str[:n] + str[n + 1:]
