#!/bin/sh

# Use redirection operator (>) to write today’s date in a file named “bmcc”. 

date > bmcc
echo "Fetched from the file bmcc-> $(cat bmcc)."
