#!/usr/bin/python3
import requests
import sys
"""Request Headers"""
if __name__ == "__main__":
    response = requests.get("https://api.github.com/user",
                            auth=(sys.argv[1], sys.argv[2]))
    if "id" in response.json():
        print(response.json().get('id'))
    else:
        print("None")
