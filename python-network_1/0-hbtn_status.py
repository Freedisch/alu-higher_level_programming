#!/usr/bin/python3
import urllib.request
""" Fetching Url """


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
