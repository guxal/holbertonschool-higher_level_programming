#!/usr/bin/python3
from urllib import request
"""Request header"""
if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        header = response.info().get('X-Request-Id')
        print(header)
