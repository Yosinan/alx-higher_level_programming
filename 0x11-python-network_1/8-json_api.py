#!/usr/bin/python3
'''
a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
-- using requests module
'''


import requests
import sys

if __name__ == '__main__':
    
    if len(sys.argv) > 1:
        d = {'q': sys.argv[1]}
    else:
        d = {'q': ""}
    
    info = requests.post('http://0.0.0.0:5000/search_user', d)
    
    try:
        json_file = info.json()
        if json_file:
            print("[{}] {}".format(json_file['id'], json_file['name']))
        else:
            print("No result")
            
    except ValueError:
        print("Not a valid JSON")
