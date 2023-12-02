#!/usr/bin/python3
""" A Python script to post to url """

import urllib.request
import sys


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    re = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(re) as response:
        print(response.read().decode('utf-8'))
