#!/usr/bin/python3
"""fetch a url response decoded in utf-8"""


from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(url) as request:
            print(request.read().decode("utf-8"))
    except HTTPError as e:
        print(f'Error code: {e.getcode()}')
