#!/bin/sh

# 4.Write a shell script to use LOGICAL OR (||) operator on two operands.For two operands “TRUE” and “FALSE”, the output should be Either of the two is TRUE.

if true || false 
then
    echo "Either of the two is TRUE"
else
    echo "Both are FALSE"
fi
 
if false || false 
then
    echo "Either of the two is TRUE"
else
    echo "Both are FALSE"
fi
