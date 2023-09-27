#!/usr/bin/python3
"""
Defines a class called Square.

Square objects have a single attribute, `size`, which is the length of
one side of the square.
"""

class Square():
    """
    Represents a square.

    Attributes:
    size: The length of one side of the square.
    """
    def __init__(self, __size=0) -> None:
        if type(__size) != int:
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = __size

    def area(self):
        return (self.__size * self.__size)
