#!/usr/bin/python3
def print_matrix_integer(maxtrix=[[]]):
    if maxtrix:
        for row in maxtrix:
            for num in row:
                print("{:d}".format(num), end=" " if num != row[-1] else "")
            print()
