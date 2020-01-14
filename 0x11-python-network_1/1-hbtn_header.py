#!/usr/bin/python3
from urllib import request
import sys
"""Request header"""
if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        header = response.info().get('X-Request-Id')
        print(header)
