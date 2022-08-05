#!/usr/bin/python3
import requests
import sys
"""Takes in Github credentials (username and password) and uses the Github API
to display an id"""


r = requests.get('https://api.github.com/user', auth=(sys.argv[2]))
if r.status_code >= 400:
    print('None')
else:
    print(r.json().get('id'))
