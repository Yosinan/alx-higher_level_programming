#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    new = set(my_list)
    for i in new:
        sum += i
    return sum
