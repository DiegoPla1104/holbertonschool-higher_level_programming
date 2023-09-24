#!/usr/bin/python3
def no_c(my_string):
    str_cp = ""
    for a in my_string:
        if a != "c" and a != "C":
            str_cp += a
    return str_cp
