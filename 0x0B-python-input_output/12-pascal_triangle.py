#!/usr/bin/python3
"""Module for generating Pascal's Triangle as a list of lists of integers"""


def pascal_triangle(n):
    """Generates Pascal's Triangle as a list of lists of integers."""
    my_list = []
    for i in range(n):
        my_list.append([])
        for j in range(i+1):
            try:
                if j - 1 == -1:
                    my_list[i].append(1)
                else:
                    my_list[i].append(my_list[i-1][j-1] + my_list[i-1][j])
            except IndexError:
                my_list[i].append(1)
    return (my_list)
