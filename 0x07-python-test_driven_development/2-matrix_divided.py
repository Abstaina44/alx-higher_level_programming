#!/usr/bin/python3

"""Module that divides every element in matrix by div"""


def matrix_divided(matrix, div):
    """Function that divides every element in matrix by div
    Args:
        matrix: Matrix argument
        div (int/float): Divisor

    Returns:
        matrix: Resultant matrix after dividing each matrix 
        element by div
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    res = []
    dim = len(matrix[0])

    for i in range(len(matrix)):
        if dim != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")

        temp = []

        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

            temp.append(round(matrix[i][j] / div, 2))

        res.append(temp)

    return res
