#!/usr/bin/python3
"""fetch the json response of a url"""


import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = {'q': {argv[1]}} if len(argv) > 1 else {'q': ""}

    response = requests.post(url, data=q)
    try:
        res = response.json()
        if res == {}:
            print("No result")
        else:
            # print(res)
            print(f'[{res.get("id")}] {res.get("name")}')
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
