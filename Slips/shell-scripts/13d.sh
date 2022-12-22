#!/bin/sh

# 4.Write a shell script to accept two numbers from user and display their multiplication and subtraction.
#            If user enters two numbers 6 and 5, the output should be
#            The multiplication of 6 and 5 is 30.
#            The subtraction of 6 and 5 is 11.    

echo "Enter two numbers: "
read -r num1 num2
echo "The multiplication of $num1 and $num2 is $((num1 * num2))."
echo "The subtraction of $num1 and $num2 is $((num1 - num2))."
