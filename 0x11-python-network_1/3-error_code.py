#!/usr/bin/python3
"""
A  Python script that takes in a URL, sends a request to the URL
 sends a request to the URL and displays the body of the response
 """

import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read()
            print("{}".format(html.decode('utf-8')))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
