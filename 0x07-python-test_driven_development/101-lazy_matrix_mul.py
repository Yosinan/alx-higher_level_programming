<<<<<<< HEAD
#!/usr/bin/python3.5
"""

Module composed by a function that multiplies 2 matrices

"""
=======
#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
>>>>>>> 282accc3142852b4b5b3e6b752cca9f58b67b4c2
import numpy as np


def lazy_matrix_mul(m_a, m_b):
<<<<<<< HEAD
    """ Function that multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of the multiplication


=======
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
>>>>>>> 282accc3142852b4b5b3e6b752cca9f58b67b4c2
    """

    return (np.matmul(m_a, m_b))
