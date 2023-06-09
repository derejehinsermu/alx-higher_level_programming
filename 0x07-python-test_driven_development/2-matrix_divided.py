#!/usr/bin/python3
""" Define a function called matrix_divided """


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number.

    Args:
        matrix (list): A list of lists representing the matrix.
                       Each inner list contains integers or floats.
        div (int or float): The number to divide the elements of the matrix by.

    Returns:
        list: A new matrix with elements divided by the given number.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   or if div is not a number.
        TypeError: If each row of the matrix does not have the same size.
        ZeroDivisionError: If div is equal to zero.

    """
    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
