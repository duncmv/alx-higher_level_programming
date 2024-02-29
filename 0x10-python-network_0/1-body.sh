#!/bin/bash
# displays the body of only 200 status code
curl -s -w "%{http_code} %{remote_ip}\n" "$1" | tail -n 1 | awk '{if($1==200) system("curl -s " $2) }'
