#!/usr/bin/python3
"""
Defines a function that reads a text file
"""


def read_file(filename=""):
    """
    Reads the contents of a text file and prints it to the
    standard output.

    Args:
        filename (str): The name of the text file to be read.
        Defaults to 'my_file_0.txt'.
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
