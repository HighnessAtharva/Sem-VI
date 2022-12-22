#!/bin/sh

# Write a shell script and check if a file /dev/mapper is a directory file or not.

if [ -d /dev/mapper ]
then
    echo "File /dev/mapper is a directory file"
else
    echo "File /dev/mapper is not a directory file"
fi