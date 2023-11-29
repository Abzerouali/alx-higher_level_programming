#!/usr/bin/python3
"""Defines a function that utilizes NumPy to efficiently multiply two matrices.

Args:
    m_a (list of lists of ints/floats): The first matrix.
    m_b (list of lists of ints/floats): The second matrix.

Returns:
    list of lists: The resulting product matrix."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))
