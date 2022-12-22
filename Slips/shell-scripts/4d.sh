#!/bin/sh

# Write a shell script and check if a file /dev/console is a block file or not.
# NEED CONFIRMATION
if [ -b /dev/console/ ]; then
    echo "File /dev/console is a block file"
else
    echo "File /dev/console is not a block file"
fi