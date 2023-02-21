#!/bin/bash

# accept a number and print its sum of digits

echo "Enter a number: "
read num

# while loop
sum=0
while [ $num -gt 0 ]
do
    rem=$((num % 10))
    sum=$((sum + rem))
    num=$((num / 10))
done

echo "Sum of digits of the number is $sum"