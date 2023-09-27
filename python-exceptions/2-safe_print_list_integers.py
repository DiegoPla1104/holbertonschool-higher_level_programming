#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nprinted = 0
    for iter in range(x):
        try:
            print("{:d}".format(my_list[iter]), end="")
            nprinted += 1
        except (ValueError, TypeError):
            pass
    print()
    return nprinted
