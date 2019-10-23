#/bin/bash
#Script to parse the logs and then convert it to json

read -p 'Enter the name of the log file which you want to parse:' file
while IFS= read -r line
do
ip=`echo $line|cut -d"," -f3`
code=$(curl -s 'http://localhost:3000/'$ip | sed 's/\\\\\//\//g' | sed 's/[{}]//g' | awk -v k="IsoCode" '{n=split($0,a,","); for (i=1; i<=n; i++) print a[i]}' |  sed 's/\"//g' | grep -i isocode | cut -d":" -f2| awk 'NF > 0'| head -n 1)
echo $line,$code >> new.log
done < $file
jq -Rs '[ split("\n")[] | select(length > 0) | split(",") | {type: .[0], date: .[1], source_ip: .[2], response_time: .[3], target_url: .[4], http_code: .[5], iso_code: .[6]}]' new.log > output1.json
