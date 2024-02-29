#!/bin/bash
# sends a POST request to the passed URL, and displays the body of the response
curl -sL -X POST -d email="test@gmail.com" -d subject="I will alwaysbe here for PLD" "$1"
