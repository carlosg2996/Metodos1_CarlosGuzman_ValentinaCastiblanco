#!/bin/bash

n=20
r=3
let resta=$n-$r

typeset -i factorial=1

while [ $n -gt 1 ]
do
	let factorial=$factorial*$n
	let n=$n-1
done


typeset -i factorialr=1

while [ $resta -gt 1 ]
do
        let factorialr=$factorialr*$resta
        let resta=$resta-1
done


let division=$factorial/$factorialr

echo $division
