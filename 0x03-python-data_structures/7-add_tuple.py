#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        ls_a = list(tuple_a)
        ls_a.extend([0] * (2 - len(tuple_a)))
        tuple_a = tuple(ls_a)
    if len(tuple_b) < 2:
        ls_b = list(tuple_b)
        ls_b.extend([0] * (2 - len(tuple_b)))
        tuple_b = tuple(ls_b)
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1] + tuple_b[1]
    return (a, b)
