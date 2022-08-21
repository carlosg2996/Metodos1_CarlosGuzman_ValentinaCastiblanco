#!/bin/bash
if [ $# -eq 0 ]; then
	echo --- Programa sin parametros ---
	echo --- Parametro 1: n-factorial ---
	exit 1
fi

n=$1

typeset -i factorial=1

if [ $n -eq 0 ] || [ $n -eq 1 ]; then
	echo El factorial de $1 es $factorial
else
	while [ $n -gt 1 ]
	do
		let factorial=$factorial*$n
		let n=$n-1
	done
	echo El factorial de $1 es $factorial
fi


