#!/usr/bin/python3
""" A Python script to take in a letter and send a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    data = {'q': q}
    re = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        if not p.json():
            print("No result")
        else:
            print("[{}] {}".format(p.json().get('id'), p.json().get('name')))
    except ValueError:
        print("Not a valid JSON")
