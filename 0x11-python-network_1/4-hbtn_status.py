#!/usr/bin/python3
""" A Python script to fetch https://intranet.hbtn.io/status """
import requests


if __name__ == "__main__":
    re = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}".format(type(re.text)))
    print("\t- content: {}".format(re.text))
