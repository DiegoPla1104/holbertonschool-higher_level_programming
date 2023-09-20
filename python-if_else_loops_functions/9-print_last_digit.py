#!/usr/bin/python3
def print_last_digit(number):
    saver = ''
    if number < 0:
        saver = ((number % 10) - 2)
    else:
        saver = (number % 10)
    print(saver, end='')
    return saver
