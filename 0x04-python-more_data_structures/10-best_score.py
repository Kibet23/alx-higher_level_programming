#!/usr/bin/python3
def best_score(a_dictionary):
    """
    returns a key with the biggest integer value
    Parameters:
    a_dictionary: to be checked
    """
    if not a_dictionary:
        return (None)

    max_key = max(a_dictionary, key=lambda k: a_dictionary[k] if isinstance(
        a_dictionary[k], int) else float('-inf'))
    return (max_key)
