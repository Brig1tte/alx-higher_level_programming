#!/usr/bin/python3
""" function to invert eq and nq in a class """


class MyInt(int):
    """ inverted equality for int class """

    def __eq__(self, other):
        if isinstance(self, type(other)):
            return False

    def __ne__(self, other):
        if isinstance(self, type(other)):
            return True
