#!/usr/bin/python3
import requests
import sys
"""Takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response"""


r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
print(r.text)
