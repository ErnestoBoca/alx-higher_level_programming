#!/usr/bin/python3
def remove_char_at(str, n):
    cpy = ""
    if (n >= 0 and n < len(str)):
        for i in str:
            if (i != str[n]):
                cpy = cpy + i
        return (cpy)
    else:
        return (str)
