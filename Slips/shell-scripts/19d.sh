#!/bin/sh

# Write a shell script to write all the files and subdirectories inside / (root) directory to a file called “tree” in present working directory. Use redirection operator to redirect output of your shell script to “tree” file. 

ls -Rl . > tree
echo "Fetched from the file tree-> $(cat tree)."
