#!/usr/bin/python3
"""
this module contains a function that divides elements of a matrix
"""


def matrix_divided(matrix, div):
    """ divides all elements of matrix by div
        Args:
            matrix (list): the matrix
            div (int): the value to divide the matrix
        Returns:
            A new matrix of elements of the matrix divided by div,
            rounded to 2 decimal places
        Raises:
            TypeError: if matrix is not a list of lists of integers or floats
            TypeError: if each row of the matrix does not have the same size
            TypeError: if div is not an integer or a float
            ZeroDivisionError: if div is 0

    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list:
        raise TypeError(msg)
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    size = len(matrix[0])
    sum_tot = []
    for row in matrix:
        if type(row) != list:
            raise TypeError(msg)
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
        sum_row = []
        for element in row:
            if type(element) != int and type(element) != float:
                raise TypeError(msg)
            sum_row.append(round(element / div, 2))
        sum_tot.append(sum_row)
    return sum_tot


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/2-matrix_divided.txt")
