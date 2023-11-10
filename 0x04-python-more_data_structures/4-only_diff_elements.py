#!/usr/bin/bash
def only_diff_elements(set_1, set_2):
    union = set()
    union = set_1 ^ set_2
    return (union)
