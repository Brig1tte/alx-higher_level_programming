#!/bin/bash
# A Bash script to send a DELETE request to the URL passed as
# the first argument and displays the body of the response
curl -X DELETE -s "$1"
