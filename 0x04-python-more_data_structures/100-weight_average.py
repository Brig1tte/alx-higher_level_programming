#!/usr/bin/python3

def weight_average(my_list=[]):
    """Return the weighted average of all integers in a list of tuples."""
    if my_list and len(my_list):
        number = 0
        denom = 0
        for tup in my_list:
            number += (tup[0] * tup[1])
            denom += (tup[1])
        return (num/denom)
    return (0)
