#!/bin/sh

# 4.Write a shell script to accept an operand from user and use increment and decrement operators on it. 
# For operand 8, the output should be
# 	8++ = 9
# 	8-- = 7       

echo "Enter a number: "
read -r num
echo "$num++ = $((num + 1))"
echo "$num-- = $((num - 1))"