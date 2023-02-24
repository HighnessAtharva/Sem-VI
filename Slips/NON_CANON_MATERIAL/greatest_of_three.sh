#!/bin/bash

# accept three numbers and print the greatest of them

echo "Enter three numbers: "
read num1 num2 num3
 

if [ $num1 -eq $num2 ] && [ $num1 -eq $num3 ] 
then
    echo "All numbers are equal"
elif [ $num1 -gt $num2 ] && [ $num1 -gt $num3 ]
then
    echo "Greatest number is $num1"
elif [ $num2 -gt $num1 ] && [ $num2 -gt $num3 ]
then
    echo "Greatest number is $num2"
else
    echo "Greatest number is $num3"
fi