#!/bin/bash
# displays the body of only 200 status code
ip=$1; curl -s -w "%{http_code}" "$ip" | tail -n 1 | awk -v ip="$ip" '{if($0==200) system("curl -s " ip) }'
