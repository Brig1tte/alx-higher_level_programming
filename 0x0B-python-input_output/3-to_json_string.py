#!/usr/bin/python3
"""
    function to return the JSON representation of an object (string):

    Prototype: def to_json_string(my_obj):
    You don’t need to manage exceptions if the object can’t be serialized
"""


import json


def to_json_string(my_obj):
    """ function is a json representantion of object """
    return json.dumps(my_obj)
