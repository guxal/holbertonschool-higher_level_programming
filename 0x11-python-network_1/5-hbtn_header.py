#!/usr/bin/python3
import requests
import sys
"""Request with Request"""
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])