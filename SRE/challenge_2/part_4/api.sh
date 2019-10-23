#!/bin/bash

cat ~/Downloads/new.log | sed 's/,/ /g' | sort -k 6,6n >> response.txt
N=$( cat response.txt | wc -l)
count=`cat ~/Downloads/new.log | grep $1 | grep $2 | wc -l`
P95=$(dc -e "$N 95 * 100 / p")
time=`awk "FNR==$P95" response.txt | awk '{print $6}' `
echo "$1, $2,$count, $time"
