#!/bin/bash

# accept two strings and compare them to see if they are equal or not

echo "Enter two strings: "
read str1 str2

if [ $str1 = $str2 ]
then
    echo "Strings are equal"
else
    echo "Strings are not equal"
fi