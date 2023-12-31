#!/usr/bin/python3
"""
    function class Student to define a student by:

    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with first_name, last_name and age:
    def __init__(self, first_name, last_name, age):
    Public method def to_json(self): that retrieves a dictionary representation
    of a Student instance (same as 10-class_to_json.py)
    You are not allowed to import any module
"""


class Student:
    """ class function to create a dict obj """

    def __init__(self, first_name, last_name, age):
        """ function initialization for Student object """
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self):
        """ function retrieves a dictionary representation """
        return self.__dict__
