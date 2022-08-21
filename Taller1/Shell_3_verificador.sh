#!/bin/bash

pass=0

read -p "numero: " v1

function checkvalue(){
	echo Es $v1
}

while [ $pass -eq 0 ]
do
	if  [ $v1 -eq 0 ]; then
		pass=1
		checkvalue
	elif [ $v1 -eq 1 ]; then
		pass=1
		checkvalue
	else
		echo "Por favor intente de nuevo"
		exit 1
fi
done





