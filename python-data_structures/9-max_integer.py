#!/usr/bin/python3
def max_integer(my_list=[]):
    if (my_list is None) or (len(my_list) < 1):
        return
    maxint = my_list[0]
    for a in my_list:
        if (maxint < a):
            maxint = a
    return maxint
