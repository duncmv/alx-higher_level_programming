#!/bin/bash
#post with Json
curl -sL -X POST -H "Content-Type: application/json" -d "$2" "$1"
