#!/usr/bin/python3
import requests
"""Request with Request"""
if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: %s" % type(r.text))
    print("\t- content: %s" % r.text)
