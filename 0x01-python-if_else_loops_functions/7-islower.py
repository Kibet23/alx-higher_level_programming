#!/usr/bin/python3
def islower(c):
    """
    check if c is a lowercase.

    Args:
        c (str): char to be checked.

    Returns:
        bool: true if c is a lowercase, false otherwise.
    """
    return ord('a') <= ord(c) <= ord('z')


# Test the function
print(islower('a'))  # True
print(islower('Z'))  # False
print(islower('1'))  # False
