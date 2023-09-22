#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    thing = sys.argv
    length = len(sys.argv)
    result = 0
    for iter in range(1, length):
            result += int(thing[iter])
    print(result)