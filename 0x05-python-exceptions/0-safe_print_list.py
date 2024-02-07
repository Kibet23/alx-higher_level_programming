#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    prints x elements of a list.
    Args:
    my_list -  contain any type (integer, string, etc.)
    x - represents the number of elements to print

    Returns:
    the real number of elements printed
    """
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end=" ")
            count += 1
    except IndexError:
        pass
    finally:
        print()
        return (count)
