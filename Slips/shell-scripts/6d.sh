#!/bin/sh

# Write a shell script and check if a file /dev/full is a character file or not.

if [ -c /dev/full ]
then
    echo "File /dev/full is a character file"
else
    echo "File /dev/full is not a character file"
fi