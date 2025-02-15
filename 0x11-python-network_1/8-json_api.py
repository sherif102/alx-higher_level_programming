#!/usr/bin/python3
"""fetch the response code of a url"""


import requests
from sys import argv

if __name__ == "__main__":
    url = "https://www.google.com"
    q = argv[1] if len(argv) > 1 else ""
    url += f'?{q}'
    print(url)
    response = requests.post(url)
    try:
        res = response.json()
        if len(res) == 0:
            print("No result")
        else:
            print(f'[{res[0].id}] {res[0].name}')
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
