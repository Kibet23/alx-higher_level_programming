#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    prints a dictionary by ordered keys
    Parameters:
    a_dictionary - dictionary to be printed
    """
    keys1 = sorted(a_dictionary.keys())
    for key in keys1:
        print(f"{key}: {a_dictionary[key]}")
