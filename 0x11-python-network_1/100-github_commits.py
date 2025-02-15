#!/usr/bin/python3
"""fetch commits history from GitHub API"""


import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    header = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    request = requests.get(url, headers=header)
    response = request.json()
    counter = 0
    while counter <= 10:
        sha = response[counter].get("sha")
        commit = response[counter].get("commit")
        author = commit.get("author").get("name")
        print(f'{sha}: {author}')
        counter += 1
