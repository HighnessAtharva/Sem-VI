#!/bin/bash

# Accept two numbers and print their GCD and LCM
echo "Enter two numbers: "
read num1 num2

# find the smaller number
if [ $num1 -lt $num2 ]
then
    smaller=$num1
else
    smaller=$num2
fi

# use while loop to find the GCD
i=1
while [ $i -le $smaller ]
do
    if [ $((num1 % i)) -eq 0 ] && [ $((num2 % i)) -eq 0 ]
    then
        gcd=$i
    fi
    i=$((i + 1))
done

# find the LCM
lcm=$((num1 * num2 / gcd))

echo "GCD of $num1 and $num2 is $gcd"
echo "LCM of $num1 and $num2 is $lcm"