#!/usr/bin/python3

def mutiply_list_map(my_list=[], number=0):
    """Funct returns list with values multiplied by a number without loops"""
    return (list(map(lambda x: x*number, my_list)))
