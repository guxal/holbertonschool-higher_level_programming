#!/usr/bin/python3
from urllib import request, parse
import sys
"""Request POST email"""
if __name__ == "__main__":
    data = parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    with request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode('utf-8'))
