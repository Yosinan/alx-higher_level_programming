#!/usr/bin/python3
'''
a Python script that takes in a URL,
sends a request to the URL and displays
the body of the response -- using requests module
'''


import requests
import sys

if __name__ == '__main__':

    result = requests.get(sys.argv[1])

    if result.status_code >= 400:
        print("Error code: {}".format(result.status_code))
    else:
        print(result.text)
