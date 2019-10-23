#/bin/bash
#Script to parse the logs and then convert it to json

read -p 'Enter the name of the log file which you want to parse:' file
jq -Rs '[ split("\n")[] | select(length > 0) | split(",") | {type: .[0], date: .[1], source_ip: .[2], response_time: .[3], target_url: .[4], http_code: .[5]}]' $file > output.json
