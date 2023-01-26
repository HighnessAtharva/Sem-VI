#!/bin/sh

# Create a directory structure abc/123/pqr, change the name of directory “pqr” from “abc” as your present working directory.

mkdir -p abc/123/pqr
cd abc || exit
mv 123/pqr/ 123/namechanged/