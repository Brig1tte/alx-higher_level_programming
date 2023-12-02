#!/usr/bin/python3
""" A Python script to take 2 arguments in order to solve a challenge """
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.\
          format(sys.argv[2], sys.argv[1])
    re = requests.get(url)
    for q, item in enumerate(re.json()):
        print("{}: {}".format(item.get("sha"),
              item.get("commit").get("author").get("name")))
        if q == 9:
            break
