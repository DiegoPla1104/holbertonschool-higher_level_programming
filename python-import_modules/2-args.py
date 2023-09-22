#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    thing = sys.argv
    length = len(sys.argv)
    if length == 1:
        print("0 arguments.")
    if length > 1:
        print("{} arguments:" .format(len(sys.argv) - 1))
    iter = 0
    for iter in range(1, length):
        print(iter, ": ", thing[iter])
