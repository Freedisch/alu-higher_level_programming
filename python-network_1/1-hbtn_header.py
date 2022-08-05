#!/usr/bin/python3
""" A script thats displays the value of the X-Request=Id variable
found in the header of the response.
"""


if __name__ == '__main__':
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        header_var = response.headers.get('X-Request-Id')
        print(header_var)

