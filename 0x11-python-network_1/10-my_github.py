#!/usr/bin/python3
'''
a Python script that takes my GitHub credentials
(username and password(PAT)) and uses the GitHub API to display my id
'''
import requests
import sys

if __name__ == '__main__':
    my_username = sys.argv[1]
    my_PAToken = sys.argv[2]

    req = requests(
        'https://api.github.com/user',
        auth=(
            my_username,
            my_PAToken))

    json_file = req.json()
    my_ID = json_file['id']

    try:
        print(my_ID)
    except BaseException:
        print("None")
