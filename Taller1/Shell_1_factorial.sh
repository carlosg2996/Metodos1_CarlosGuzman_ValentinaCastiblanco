#!/bin/bash

n=8

typeset -i factorial=1

if [ $n -eq 0 ] || [ $n -eq 1 ]; then
	echo El factorial de $n es $factorial 
else
	while [ $n -gt 1 ]
	do
		let factorial=$factorial*$n
		let n=$n-1
	done
	echo El factorial es $factorial
fi
