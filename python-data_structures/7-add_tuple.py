#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    aa = tuple_a or (0, 0)
    bb = tuple_b or (0, 0)
    if len(tuple_a) == 1:
        aa = (tuple_a[0], 0)
    if len(tuple_b) == 1:
        bb = (tuple_b[0], 0)
    return(aa[0] + bb[0], aa[1] + bb[1])
