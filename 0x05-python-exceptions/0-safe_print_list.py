#!/usr/bin/python3

"""
safe_print_list - prints x elements of a list
@x: elements to be printed
"""


def safe_print_list(my_list=[], x=0):
    printedElements = 0


    try:
        for i in range(x):
            print(my_list[i], end=" ")
            printedElements += 1

    except IndexError:
        pass
    print()
    return printedElements
