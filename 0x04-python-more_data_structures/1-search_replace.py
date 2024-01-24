#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurences of an element by another in a new list
    Parameters:
    my_list - original list
    search - element to be replaced
    replace - element to replace the replaced element
    """
    l_list = [replace if y == search else y for y in my_list]
    return (l_list)
