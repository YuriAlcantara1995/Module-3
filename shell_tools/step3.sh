#!/bin/bash

i="0"
res=""


while [[ $res != "Something went wrong" ]] 
do
res=$(bash fails_rarely.sh)
i=$[$i+1]
echo $res >> outputStep3
done
echo "Steps: $i"
