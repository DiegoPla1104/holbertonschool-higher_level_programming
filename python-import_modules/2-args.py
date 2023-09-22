#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    thing = sys.argv
    length = len(sys.argv)
    if length == 1:
        print("0 arguments.")
    if length == 2:
        print("1 argument:")
        print(f"{iter}: {thing[iter]}")
    if length > 2:
        print("{} arguments:" .format(len(sys.argv) - 1))
    iter = 0
    for iter in range(1, length):
        print(f"{iter}: {thing[iter]}")
