#!/usr/bin/python3
""" This is a Python script that takes in a URL
sends a request to the URL and displays the value of the variable
"""

import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print("{}".format(r.headers.get('X-Request-Id')))
