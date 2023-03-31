#!/usr/bin/python3
"""
 Python script that takes in a URL, sends a request to the URL
 and manage HTTP Errors

"""

import sys
import urllib.request

if __name__ == '__main__':

    req = urllib.request.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
