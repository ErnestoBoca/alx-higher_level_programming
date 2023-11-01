#!/usr/bin/python3
for i in range(122, 96, -1):
    c = i
    if (c % 2 == 1):
        c = c - 32
    print("{}".format(chr(c)), end='')
