#!/usr/bin/python3
"""defines My list"""


class MyList(list):
    """inherits from List"""

    def print_sorted(self):
        """prints the list, but sorted in ascending sort"""

        sorted_list = sorted(self)
        print(sorted_list)
