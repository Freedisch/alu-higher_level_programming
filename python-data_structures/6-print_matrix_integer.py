#!/usr/bin/python3
def print_matrix_integer(maxtrix=[[]]):
    if maxtrix:
        for row in maxtrix:
            line_to_print = ""
            for num in row:
                line_to_print += str(num) + " "
            print(line_to_print)