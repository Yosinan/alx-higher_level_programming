#!/usr/bin/python3
""" Finds Peak values from the given lists of integers """


def find_peak(list_of_integers):
    """Find the peak"""
    list_l = len(list_of_integers)
    if list_l == 0:
        return None
    peak = binary_search(list_of_integers, 0, list_l - 1)
    return list_of_integers[peak]


""" binary search algorithim """
def binary_search(a, low, high):
    """ recursive binary search of the peak"""
    if low >= high:
        return low
    mid = ((high - low) // 2) + low
    if a[mid] > a[mid + 1]:
        return binary_search(a, low, mid)
    else:
        return binary_search(a, mid + 1, high)
