#!/usr/bin/python3
"""Defines a function for performing object attribute lookup."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
