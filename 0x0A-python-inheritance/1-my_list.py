#!/usr/bin/python3
""" function to write class MyList that inherits from list """


class MyList(list):
    """ MyList inherits from list """

    def print_sorted(self):
        """ function to print list in ascending order """
        print(sorted(self))
