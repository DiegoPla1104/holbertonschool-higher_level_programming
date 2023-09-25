#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    result = str(sorted(a_dictionary, key=lambda key: a_dictionary[key]))
    print(result)
