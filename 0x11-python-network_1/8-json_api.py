#!/usr/bin/python3
import requests
import sys
"""Request Headers"""
if __name__ == "__main__":
    if len(sys.argv) == 2:
        ul2 = "http://0.0.0.0:5000/search_user"
        url = "http://5c332d577923.41.hbtn-cod.io:5000/search_user"
        try:
            d = {'q': sys.argv[1]}
        except Exception:
            d = {'q': ""}

        r = requests.post(ul2, data=d)
        try:
            json = r.json()
            try:
                print("["+str(json['id'])+"]"+" "+json['name'])
            except KeyError:
                print("No result")
        except Exception:
            print("Not a valid JSON")
    else:
        print("No result")
