#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    _sum = 0
    for i in range(1, argc):
        _sum = _sum + int(sys.argv[i])
    print("{:d}".format(_sum))
