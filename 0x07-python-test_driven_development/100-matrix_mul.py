#!/usr/bin/python3
"""defines a function that multiplies 2 matrices
It validates the arguments first before multiplication
"""


def matrix_mul(m_a, m_b):
    """This Function multiplies two matrices after validating
    """
    mats = {"m_a": m_a, "m_b": m_b}
    err4 = "{} should contain only integers or floats"
    err5 = "each row of {} must be of the same size"

    for key, value in mats.items():
        if type(value) is not list:
            raise TypeError("{} must be a list".format(key))

    for key, value in mats.items():
        for i in value:
            if type(i) is not list:
                raise TypeError("{} must be a list of lists".format(key))

    for key, value in mats.items():
        if value == [] or value[0] == []:
            raise ValueError("{} can't be empty".format(key))

    for key, value in mats.items():
        for i in value:
            for elem in i:
                if type(elem) not in (int, float):
                    raise TypeError(err4.format(key))

    for key, value in mats.items():
        for i in value:
            if len(i) != len(value[0]):
                raise TypeError(err5.format(key))

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new = []
    for i in range(len(m_a)):
        x = []
        for j in range(len(m_b[0])):
            val = 0
            for k in range(len(m_b)):
                val += m_a[i][k] * m_b[k][j]
            x.append(val)
        new.append(x)

    return new
