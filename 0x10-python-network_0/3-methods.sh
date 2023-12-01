#!/bin/bash
# A Bash script to take in a URL & displays all HTTP methods the server accepts
curl -sI "$1" | grep "Allow " | cut -d" " -f 2-
