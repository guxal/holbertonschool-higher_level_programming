#!/usr/bin/python3
import requests
import sys
"""Request Headers"""
if __name__ == "__main__":
    if len(sys.argv) == 2:
        r = requests.post("http://0.0.0.0:5000/search_user",
                          data={'q': sys.argv[1]})
        try:
            json = r.json()
        except Exception:
            print("Not a valid JSON")

        if ['id', 'name'] is not json:
            print("No result")
        else:
            print("["+str(json['id'])+"]"+" "+json['name'])
    else:
        print("No result")
