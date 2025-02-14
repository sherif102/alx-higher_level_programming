#!/usr/bin/python3
"""fetch the value of X-Request-Id"""


import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers["X-Request-Id"])
