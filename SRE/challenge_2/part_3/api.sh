#!/bin/bash

count=`cat ~/Downloads/new.log | grep $1 | grep $2| wc -l`
#echo $count

echo -e "
{
	country :$1,\n
	date :$2,\n
	count :$count
}"
