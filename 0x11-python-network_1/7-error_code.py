#!/usr/bin/python3
import requests
import sys
"""Request Headers"""
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code == 200:
        print(r.text)
    else:
        print("Error code: %s" % r.status_code)
