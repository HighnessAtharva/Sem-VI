#!/bin/sh

# 4.Write a shell script to take input of two integers from user and display their addition and subtraction.
#         Ex.: If user enters two numbers 6 and 5, the output should be
#         The addition of 6 and 5 is 11.
#         The subtraction of 6 and 5 is 1.

echo "Enter two number: "
read -r a b
echo "The addition of $a and $b is $((a + b))"
echo "The subtraction of $a and $b is $((a - b))"