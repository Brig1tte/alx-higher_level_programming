#!/usr/bin/python3
"""
    class Student that defines a student by: (based on 10-student.py)

    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with first_name, last_name and age:
    def __init__(self, first_name, last_name, age):
    Public method def to_json(self, attrs=None): that retrieves a dictionary
    representation of a Student instance (same as 8-class_to_json.py):
        If attrs is a list of strings, only attributes name contain in this list
        must be retrieved. Otherwise, all attributes must be retrieved
    Public method def reload_from_json(self, json): that replaces all attributes
    of the Student instance: You can assume json will always be a dictionary
        A dictionary key will be the public attribute name
        A dictionary value will be the value of the public attribute
    You are not allowed to import any module

    Now, you have a simple implementation of a serialization and deserialization
    mechanism (concept of representation of an object to another format, without
    losing any information and allow us to rebuild an object based on this rep.)
"""


class Student:
    """ class function to create a dict obj / rep of a student """

    def __init__(self, first_name, last_name, age):
        """ function initialization for Student object """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ function retrieves a dictionary representation of obj attrs """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}


    def reload_from_json(self, json):
        """ function replaces all attrs of the student instance given json obj """
        for key, value in json.items():
            setattr(self, key, value)
