#!/bin/bash

pass=0

function checkvalue(){
	if [ $var -eq 0 ] || [ $var -eq 1 ]; then
		pass=1
		echo "Es "$var

	else
		echo "Por favor intente de nuevo"
		exit 1
	fi
}

while read var;
do
	if  [ $pass -eq 0 ]; then
		checkvalue $var

	else
		exit 1
	fi
done <<< $1






