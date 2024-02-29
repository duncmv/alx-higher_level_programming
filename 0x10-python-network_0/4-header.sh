#!/bin/bash
# sends a get request with custom header
curl -sL -X GET -H "X-School-User-Id: 98" "$1"
