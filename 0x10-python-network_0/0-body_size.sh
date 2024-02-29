#!/bin/bash
# displays the size of the body of response from a url
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
