#!/usr/bin/python3
"""Module for appending lines to a file after specific search strings"""


def append_after(filename="", search_string="", new_string=""):
    """Append a line of text to a file after each line containing a specific search string."""
    mod_content = ""
    with open(filename, "r") as f:
        for line in f:
            mod_content += line
            if search_string in line:
                mod_content += new_string
    with open(filename, "w") as f:
        f.write(mod_content)
