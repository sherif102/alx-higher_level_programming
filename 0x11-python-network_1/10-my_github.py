#!/usr/bin/python3
"""authenticate into github API and fetch data"""


import requests
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    password = argv[2]
    header = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {password}',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    request = requests.get("https://api.github.com/user", auth=(user, password), headers=header)
    response = request.json()
    id = response.get("id")
    print(id)
