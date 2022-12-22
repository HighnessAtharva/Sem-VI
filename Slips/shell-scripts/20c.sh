#!/bin/sh

# Create directory structure abc/123/pqr, change the name of directory “abc” from “pqr” as your present working directory.  

mkdir -p abc/123/pqr
cd abc/123/pqr || exit
mv ../../../abc ../../../melody


