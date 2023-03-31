#!/usr/bin/python3
# a pyhthon script that will list 10 commits (from the most recent to
# oldest) of the repository “rails” by the user “rails”

import sys
import requests

if __name__ == '__main__':

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    res = requests.get('https://developer.github.com/v3/repos/commits/')
    result = res.json()
    for i in (0, 10):
        print("{}: {}".format(result['id'], result['name']))
