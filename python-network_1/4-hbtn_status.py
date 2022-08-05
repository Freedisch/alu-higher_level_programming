#!/usr/bin/python3
import requests
"""Fetches https://intranet.hbtn.io/status """


r = requests.get('https://intranet.hbtn.io/status')
print('Body response:')
print('\t- type: {}'.format(type(r.text)))
print('\t- content: {}'.format(r.text))