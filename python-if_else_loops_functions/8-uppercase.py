#!/usr/bin/python3
def uppercase(str):
    saver = ''
    for iter in str:
        if ord(iter) < 123 and ord(iter) > 96:
            saver += chr(ord(iter) - 32)
        else:
            saver += chr(ord(iter))
    print(f"{saver}")
    print("")
