#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    """Funct to compute the square value of all int of a matrix using map"""
    return list(map((lambda row: list(map((lambda x: x * x), row))), matrix))
