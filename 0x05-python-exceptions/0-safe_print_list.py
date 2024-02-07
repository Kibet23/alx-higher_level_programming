#!/usr/bin/python3

"""
safe_print_list - prints x elements of a list
@x: elements to be printed
"""


def safe_print_list(my_list=[], x=0):
    try:
        printedElements = 0
        for i in my_list:
            if printedElements < x:
                print(i, end=" ")
                printedElements += 1
        print()
        return printedElements
    except IndexError:
        pass
