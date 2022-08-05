#!/usr/bin/python3
import urllib.request
from urllib.error import HTTPError
import sys
"""Takes in a URL, sends a request to the URL and
displays the body of the response"""



try:
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.read().decode("utf-8", "replace"))
except HTTPError as e:
    print("Eror code: {}".format(e.code))
