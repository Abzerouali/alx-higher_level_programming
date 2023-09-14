#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        n = 0
        dem = 0
        for tup in my_list:
            n += (tup[0] * tup[1])
            dem += tup[1]
        return (n / dem)
    return 0
