#!/usr/bin/python3
"""
 a function that writes a string to a text file
"""


 def write_file(filename="", text=""):
    """
    Writes the specified text to a file with the given filename.

    Args:
        filename (str): The name of the file to write the text to.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
