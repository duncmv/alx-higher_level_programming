#!/bin/bash
# displays the size of the body of response from a url
curl -sI -X OPTIONS "$1" | grep -i Allow | awk '{print $2}'
