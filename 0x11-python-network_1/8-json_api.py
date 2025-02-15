#!/usr/bin/python3
"""fetch the json response of a url"""


import requests
from sys import argv

if __name__ == "__main__":
    url = "https://www.google.com"
    q = {'q': {argv[1]}} if len(argv) > 1 else {}

    response = requests.post(url, data=q)
    try:
        res = response.json()
        if not res:
            print("No result")
        else:
            # print(res)
            print(f'[{res.id}] {res.name}')
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
