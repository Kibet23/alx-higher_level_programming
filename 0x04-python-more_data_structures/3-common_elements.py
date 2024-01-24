#!/usr/bin/python3
def common_elements(set_1, set_2):
    """"
    returns a set of common elements in two sets
    Parameters:
    set_1 - first set
    set_2 - second set
    Return:
    common elements in two sets
    """
    common_set = set_1.intersection(set_2)
    return (common_set)
