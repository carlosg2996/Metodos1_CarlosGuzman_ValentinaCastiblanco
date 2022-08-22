#!/bin/bash

declare -a array

i=0
while read line;
do

	array+="$line";
	array[$i]="$line"
	let i++
done < rutas.txt

echo ${array[2]}
