#!/bin/bash

# accept a number and print whether it is odd or even

echo "Enter a number: "
read num

if [ $((num % 2)) -eq 0 ]
then
    echo "Number is even"
else
    echo "Number is odd"
fi