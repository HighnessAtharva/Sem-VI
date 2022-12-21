#!/bin/sh

# Write a shell script to take input of two integerrs from user and display their modulus and multiplication.
# If user enters two numbers 6 and 5, the output should be
# The modulus of 6 and 5 is 1.
# The multiplication of 6 and 5 is 30.   

 
echo "Enter two numbers: "
read -r num1 num2
echo "multiplication of $num1 * $num2 = $((num1 * num2))"

 