#!/usr/bin/python3
"""
Fetches and displays the X-Request-Id header from a given URL.

Usage:
    python3 1-hbtn_header.py <URL>

Arguments:
    URL (str): The URL to fetch.

Output:
    Prints the value of the "X-Request-Id" header if present.

"""


import urllib.request
from sys import argv


with urllib.request.urlopen(argv[1]) as response:
    """fetch the request-id of a url"""
    print(response.headers["X-Request-Id"])
