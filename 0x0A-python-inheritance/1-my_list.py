#!/usr/bin/python3
"""
a class MyList that inherits from list
"""


class MyList(list):
    """
        Sorts the elements of the list instance in ascending
        order and prints the sorted result.

        Parameters:
        None

        Returns:
        None
        """

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
