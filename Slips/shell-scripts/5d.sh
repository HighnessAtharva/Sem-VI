#!/bin/sh

# Write a shell script to take input of two integers from user and display their subtraction and comparison.
# If user enters two numbers 6 and 5, the output should be
# The subtraction of 6 and 5 is 1.
# 6 is greater than 5.

echo "Enter two number: "
read -r a b
echo "The subtraction of $a and $b is $((a - b))"
if [ "$a" -gt "$b" ]; then
    echo "$a is greater than $b"
elif [ "$a" -eq "$b" ]; then
    echo "$a is equal to $b"
else
    echo "$a is less than $b"
fi