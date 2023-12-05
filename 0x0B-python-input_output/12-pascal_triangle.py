#!/usr/bin/python3
""" 
Module that defines a function to generate Pascal's Triangle.

Pascal's Triangle is a mathematical construct where each number is the sum 
of the two numbers directly above it in the previous row, with the first and 
last number in each row being 1.
"""

def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal's"""
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
