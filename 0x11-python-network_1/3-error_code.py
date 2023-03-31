#!/usr/bin/python3

''' a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8) '''

import sys
import urllib

if __name__ == "__main__":

    URL = sys.argv[1]
    try:
        with urllib.request.urlopen(URL) as request:
            req = request.read().decode('UTF8')
        print(req)

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
