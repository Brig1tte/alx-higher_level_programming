#!/bin/bash
# A Bash script to display the size (in bytes) of the body of the response
curl -Is "$1" | grep -i content-length | cut -d: -f2 | tr -d " "
