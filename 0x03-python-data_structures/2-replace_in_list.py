#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position (like in C)."""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
