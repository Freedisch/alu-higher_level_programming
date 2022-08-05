#!/usr/bin/python3
import urllib.request
import sys
""" Response header """


with urllib.request.urlopen(sys.argv[1]) as response:
    """Documented"""

    
    head = response.headers.get('X-Request-Id')
    print(head)
