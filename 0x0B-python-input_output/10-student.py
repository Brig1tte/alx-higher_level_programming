#!/usr/bin/python3
"""
    class Student function to define a student by: (based on 9-student.py)

    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with first_name, last_name and age:
    def __init__(self, first_name, last_name, age):
    Public method def to_json(self, attrs=None): that retrieves a dictionary
    representation of a Student instance (same as 8-class_to_json.py):
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved Otherwise, all attributes must be retri'vd
    You are not allowed to import any module
"""


class Student:
    """ class function to create a dict obj """

    def __init__(self, first_name, last_name, age):
        """ function initialization for Student object """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ function retrieves a dictionary representation of a student """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
