#!/bin/bash
# returns status code of URL request
curl -sL -w "\n%{http_code}" "$1" | tail -n 1
