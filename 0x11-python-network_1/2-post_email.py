#!/usr/bin/python3
"""send a post request to a url and email then display the response"""

from urllib.request import urlopen
from urllib import parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = {'email': f'{argv[2]}'}
    data = parse.urlencode(email)
    data = data.encode('ascii')
    with urlopen(url, data) as request:
        print(request.read().decode("utf-8"))
