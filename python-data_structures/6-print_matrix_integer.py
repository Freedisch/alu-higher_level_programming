#!/usr/bin/python3
def print_matrix_integer(maxtrix=[[]]):
    if maxtrix:
        for row in maxtrix:
            line_to_print = ""
            for num in row:
                print("{:d}".format(num), end=" " if num !=[-1] else "")
            print()
