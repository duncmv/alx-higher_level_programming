#!/bin/bash
# displays the size of the body of response from a url
curl -s -w "%{size_download}\n" "$1" | tail -n 1
