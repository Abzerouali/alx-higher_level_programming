#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(1)
        else:
            new_list.append(0)
    return new_list
