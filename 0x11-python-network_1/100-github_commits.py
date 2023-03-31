#!/usr/bin/python3
# a pyhthon script that will list 10 commits (from the most recent to
# oldest) of the repository “rails” by the user “rails”

from sys import argv
import requests

if __name__ == '__main__':

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    res = requests.get('https://api.github.com/repos/{}/{}/commits'
                       .format(owner_name, repo_name))
    js = res.json()
    for i in js[0:10]:
        print(
            "{}: {}".format(
                i.get('sha'),
                i.get('commit').get('author').get('name')))
