#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        is_mul = []
        for num in my_list:
            if num % 2 == 0:
                is_mul.append(True)
            else:
                is_mul.append(False)
        return is_mul
