#!/usr/bin/python3
"""
Module: 1-hbtn_header.py
Author: Sheriff Abdulfatai
"""


import urllib.request
from sys import argv

with urllib.request.urlopen(argv[1]) as response:
    print(response.headers["X-Request-Id"])
