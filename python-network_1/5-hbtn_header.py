#!/usr/bin/python3
import requests
import sys


r = requests.get(sys.argv[1])
print(r.headers.get('X-Request-Id'))
