#!/usr/bin/python3
"""
A Python script to take in a URL, sends a request to the URL and display
the value of the variable X-Request-Id in the response header
"""
import requests
import sys


if __name__ == "__main__":
    re = requests.get(sys.argv[1])
    print(re.headers.get('X-Request-Id'))
