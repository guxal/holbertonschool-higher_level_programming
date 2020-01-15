#!/usr/bin/python3
import requests
import sys
"""Request Headers"""
if __name__ == "__main__":
    r = requests.get('https://swapi.co/api/people/',
                     params={'search': sys.argv[1]})
    dj = r.json()
    print("Number of results:", dj.get("count"))
    for rl in dj.get('results'):
        print(rl.get('name'))
