#!/usr/bin/python3

def best_score(a_dictionary):
    key = None
    best = -1
    if (a_dictionary is None):
        return key
    for c, d in a_dictionary.items():
        if d > best:
            best = d
            key = c
    return key
