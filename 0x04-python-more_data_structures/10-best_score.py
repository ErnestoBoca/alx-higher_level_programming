#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None):
        return (None)
    else:
        best_k = ""
        best_s = 0
        for k, v in a_dictionary.items():
            if (v > best_s):
                best_k = k
                best_s = v
    return (best_k)
