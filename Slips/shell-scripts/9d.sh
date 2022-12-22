#!/bin/sh

# Write a shell script to take input of two integers from user and compare them and display which one is greater.
#        If user enters two numbers 6 and 5, the output should be
#        6 is greater than 5.    

echo "Enter two numbers: "
read -r num1 num2
 
if [ "$num1" -gt "$num2" ]
then
    echo "$num1 is greater than $num2"
elif [ "$num1" -eq "$num2" ]
then
    echo "$num1 is equal to $num2"
else
    echo "$num2 is greater than $num1"
fi