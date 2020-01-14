#!/usr/bin/python3
import urllib.request
"""This request with urllib"""
if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("    - type: "+str(type(html)))
        print("    - content: "+str(html))
        print("    - utf8 content: "+html.decode('utf-8'))
