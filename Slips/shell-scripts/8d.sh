#!/bin/sh

# Write a shell script to use LOGICAL AND (&&) operator on two operands.
#         For two operands “TRUE” and “FALSE”, the output should be 
#         Both are not TRUE.     

if  true  &&  false 
then
    echo "Both are TRUE"
else
    echo "Both are not TRUE"
fi

if true  &&  true 
then
    echo "Both are TRUE"
else
    echo "Both are not TRUE"
fi

