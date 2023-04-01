#!/usr/bin/python3
'''
a pyhthon script that will list 10 commits (from the most recent to
oldest) of the repository “rails” by the user “rails”
'''
import requests
import sys

if __name__ == '__main__':

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner_name, repo_name)
    res = requests.get(url)
    js = res.json()
    for i in sorted(js, key=lambda c: c.get('commit')
                    .get('author').get('date'), reverse=True)[0:10]:
        print(
            "{}: {}".format(
                i.get('sha'),
                i.get('commit').get('author').get('name')))
