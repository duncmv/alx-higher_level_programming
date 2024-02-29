#!/bin/bash
# sends a DELETE request to the URL passed as the first argument
curl -sL "$1" -X DELETE 
