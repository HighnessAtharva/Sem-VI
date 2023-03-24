#!/bin/bash

# accept a number and print its reverse
echo "Enter a number: "
read num
 
# while loop
while [ $num -gt 0 ]
do
    rem=$((num % 10))
    rev=$((rev * 10 + rem))
    num=$((num / 10))
done
 
echo "Reverse of the number is $rev"