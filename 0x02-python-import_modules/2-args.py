#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenght = len(sys.argv)
    if (lenght == 1):
        print("0 arguments.")
    elif (lenght == 2):
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(lenght - 1))
        for i in range(1, lenght):
            print("{:d}: {}".format(i, sys.argv[i]))
