#!/usr/bin/python3
""" A function that finds a peak in a list of unsorted integers """

def find_peak(list_of_integers):
    """ call recursive function """
    if list_of_integers is None or list_of_integers == []:
        return None
    length = len(list_of_integers)
    return find_recursively(list_of_integers, 0, length - 1, length)


def find_recursively(lists, low, hi, length):
    """ recursively find the peak """
    mid = (low + hi)/2
    mid = int(mid)
    if (mid == 0 or lists[mid - 1] <= lists[mid])\
            and (mid == (length - 1) or lists[mid + 1] <= lists[mid]):
                return lists[mid]
    elif mid > 0 and lists[mid - 1] > lists[mid]:
        return find_recursively(lists, low, mid - 1, length)
    else:
        return find_recursively(lists, mid + 1, hi, length)
