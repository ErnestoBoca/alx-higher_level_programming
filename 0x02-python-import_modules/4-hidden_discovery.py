#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hd
    names = dir(hd)
    for n in names:
        if (n[:2] != "__"):
            print(n)
