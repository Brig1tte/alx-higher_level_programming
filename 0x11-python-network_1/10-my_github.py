#!/usr/bin/python3
""" A Python script to take your GitHub credentials (username and password)
and use the GitHub API to display your id """
import requests
import sys


if __name__ == "__main__":
    auth = (sys.argv[1], sys.argv[2])
    re = requests.get('https://api.github.com/user', auth=auth)
    print(re.json().get('id'))
