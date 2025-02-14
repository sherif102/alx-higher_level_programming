#!/usr/bin/python3
"""send requst with post method with email"""


import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = {"email": f'{argv[2]}'}

    response = requests.get(argv[1], email)
    print(response.text)
