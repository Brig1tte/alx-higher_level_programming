#!/usr/bin/python3
""" function to define a class Square that inherits from Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ function to represent a square """

    def __init__(self, size):
        """ function to Initialize a square instance """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Computes the area of the square """
        return self.__size ** 2

    def __str__(self):
        """ function to return the string representation of the square """
        return f"[Square] {self.__size}/{self.__size}"
