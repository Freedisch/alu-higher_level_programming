#!/usr/bin/python3
import requests
import sys
"""Takes in Github repo nd owner name to list
10 commits (from the most recent to oldest)"""


r = requests.get('https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2], sys.argv[1]))
if r.status_code >= 400:
    print('None')
else:
    for com in r.json()[:10]:
        print("{}: {}".format(com.get('sha'), com.get('sha'), com.get('commit').get('author').get('name')))
