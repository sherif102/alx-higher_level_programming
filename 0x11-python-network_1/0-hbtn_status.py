#!/usr/bin/python3
"""
Module: 0-hbtn_status.py
Author: Sheriff Abdulfatai
"""


from urllib.request import Request, urlopen
request = Request('https://alx-intranet.hbtn.io/status')
with urlopen(request) as request:
    html = request.read()
    print("Body response:")
    print(f'\t- type: {type(html)}')
    print(f'\t- content: {html}')
    print(f'\t- utf8 content: {(html.decode("utf-8"))}')
