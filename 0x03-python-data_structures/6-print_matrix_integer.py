#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for num in matrix[i]:
            print("{:d}".format(num), end=" ")
        print()
