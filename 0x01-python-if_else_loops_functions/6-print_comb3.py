#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if (i != j):
            if (i == 0 and j == 1):
                print("{}{}".format(i, j), end='')
            else:
                print(", {}{}".format(i, j), end='')
print()
