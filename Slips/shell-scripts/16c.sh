#!/bin/sh

# Use binary calculator to perform multiplication and division of any two integers.      

echo "Enter two numbers: "
read -r num1 num2
echo "The multiplication of $num1 and $num2 is $(echo "$num1 * $num2" | bc)."
echo "The division of $num1 and $num2 is $(echo "$num1 / $num2" | bc)."
