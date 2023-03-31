#!/usr/bin/python3
'''
a Python script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header

'''


import requests
import sys

if __name__ == '__main__':

    URL = sys.argv[1]
    res = requests.get(URL)
    header = res.headers.get('X-Request-Id')

    print(header)
