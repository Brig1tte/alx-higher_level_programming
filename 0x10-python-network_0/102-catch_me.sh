#!/bin/bash
# A Bash script to make a request to 0.0.0.0:5000/catch_me to cause the server
# to respond with a message containing You got me!, in the body of the response
curl -s -X PUT -d "user_id=98" -L -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
