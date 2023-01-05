#!/bin/sh

# Create a directory structure abc/pqr/xyz/def, make your present working directory abc/pqr/xyz/def, and then change your present working directory to /etc/hosts using RELATIVE PATH.    

mkdir -p abc/pqr/xyz/def
cd abc/pqr/xyz/def || exit
echo "Current Directory-> $(pwd)"

cd ~/../../etc/ || exit
echo "Current Directory-> $(pwd)"
mkdir host1
cd host1 || exit
echo "Current Directory-> $(pwd)"