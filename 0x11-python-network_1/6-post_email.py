#!/usr/bin/python3
"""
A Python script to take in a URL & an email address, send a POST request to the
passed URL with the email as a parameter, and display the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    re = requests.post(sys.argv[1], data=data)
    print(re.text)
