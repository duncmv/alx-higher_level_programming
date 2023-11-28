#!/usr/bin/python3
import numpy as np
"""This is a lazy matrix module using NumPy
"""


def lazy_matrix_mul(m_a, m_b):

    if not isinstance(m_a, np.ndarray):
        raise TypeError("m_a must be a numpy array")
    if not isinstance(m_b, np.ndarray):
        raise TypeError("m_b must be a numpy array")

    return np.dot(m_a, m_b)
