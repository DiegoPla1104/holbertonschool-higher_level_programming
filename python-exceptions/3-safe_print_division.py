#!/usr/bin/python3
def safe_print_division(a, b):
    global result
    result = 0
    try:
        result = a / b
    except (ValueError, TypeError, IndexError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
