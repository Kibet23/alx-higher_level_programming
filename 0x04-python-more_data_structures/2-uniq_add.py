#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    adds all unique integers in a list
    Parameters:
    my_list[]: list of integers.
    Return:
    Sum of all unique integers in a list
    """
    unique_int = set(my_list)
    result = sum(unique_int)
    return (result)
