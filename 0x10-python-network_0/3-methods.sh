#!/bin/bash
# displays the allowed methods
curl -sLI "$1" | grep -i Allow | awk '{sub($1" ", ""); print}'
