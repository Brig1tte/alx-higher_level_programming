#!/usr/bin/python3

def no_c(my_string):
    """Remove all characters c and C from a string."""
    COPY = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
