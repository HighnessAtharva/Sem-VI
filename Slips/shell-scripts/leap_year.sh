#!/bin/bash

# accept a year and print whether it is a leap year or not

echo "Enter a year: "
read year
 
if [ $((year % 4)) -eq 0 ]
then
    echo "Year is a leap year"
else
    echo "Year is not a leap year"
fi