#!/usr/bin/python3
"""
This module provides a function to indent text based on punctuation marks.

The `text_indentation` function takes a string `text` as input and splits it into lines, indenting each line after a question mark, exclamation mark, or period.

Args:
    text (str): The text to be indented.

Raises:
    TypeError: If `text` is not a string.
"""


def text_indentation(text):
    """splits a text into lines along "?", ":", "." followed by 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")
