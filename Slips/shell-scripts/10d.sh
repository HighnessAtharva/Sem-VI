#!/bin/sh

# Write a shell script to accept two numbers from user and display their addition and increment.                                               
#         If user enters two numbers 6 and 5, the output should be
#        The subtraction of 6 and 5 is 11.
#         5++ =  6
#         6-- = 5     

echo "Enter two numbers: "
read -r num1 num2
 
echo "The addition of $num1 and $num2 is $((num1 + num2))"
echo "$num1++ = $((num1+1))"
echo "$num2-- = $((num2-1))"