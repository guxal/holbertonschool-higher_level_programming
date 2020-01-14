#!/usr/bin/python3
import requests
import sys
"""Request Headers"""
if __name__ == "__main__":
    if len(sys.argv) == 2:
        ul2 = "http://0.0.0.0:5000/search_user"
        url = "http://5c332d577923.41.hbtn-cod.io:5000/search_user"
        r = requests.post(url2, data={'q': sys.argv[1]})
        try:
            json = r.json()
        except Exception:
            print("Not a valid JSON")

        try:
            print("["+str(json['id'])+"]"+" "+json['name'])
        except KeyError:
            print("No result")
    else:
        print("No result")
