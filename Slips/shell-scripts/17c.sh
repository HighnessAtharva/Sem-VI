#!/bin/sh

# List all the directories except . and .. 

# NEED CONFIRMATION

for dir in $(ls -d */)
do
    # Remove the trailing slash
    dir=${dir%?}
    # Get the size of the directory
    size=$(du -sh "$dir" | cut -f1)
    # Print the directory name and size
    echo "$dir: $size"
done