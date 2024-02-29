#!/bin/bash
# returns status code of URL request
curl -sL -w "%{http_code}" -o /dev/null "$1"
