#!/bin/sh

# Write a shell script and check if a file /dev/tty7 is a character file or not.

if [ -c /dev/tty7 ]
then
    echo "/dev/tty7 is a character file"
else
    echo "/dev/tty7 is not a character file"
fi