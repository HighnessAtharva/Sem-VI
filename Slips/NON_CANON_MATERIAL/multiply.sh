#!/bin/bash

# accept a number and print its multiplication table

echo "Enter a number: "
read num
 
echo "Enter a range for multiplication:"
read range

# while loop
i=1
while [ $i -le $range ]
do
    echo "$num * $i = $((num * i))"
    i=$((i + 1))
done
