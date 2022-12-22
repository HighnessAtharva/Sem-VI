#!/bin/sh

# Create a directory structure abc/123/pqr, change the name of directory “pqr” from “abc” as your present working directory. 
# NEED CONFIRMATION

mkdir -p abc/123/pqr
cd abc/123/ || exit
mv pqr xyz

