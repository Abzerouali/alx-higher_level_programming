#!/usr/bin/python3
"""
Module for defining the append_after function.

The append_after function appends a line of text to a file after each line
that contains a specific string.
"""
def append_after(filename="", search_string="", new_string=""):
    """Append a line of text to a file, after
     each line containing a specific string"""
    new_content = ""
    with open(filename, "r") as f:
        for line in f:
            new_content += line
            if search_string in line:
                new_content += new_string
    with open(filename, "w") as f:
        f.write(new_content)
