#!/bin/sh

# Create a directory structure abc/pqr/xyz/def, make your present working directory abc/pqr/xyz/def, and then change your present working directory to /etc/hosts using RELATIVE PATH.    

echo "Current Directory-> $(pwd)"

mkdir -p abc/pqr/xyz/def
cd abc/pqr/xyz/def || exit
echo "Current Directory-> $(pwd)"

# For me, this file resides in /mnt/c/Users/AtharvaShah/Desktop/Sem6/Sem-VI/Slips/shell-scripts. 
# Change this path to suit your needs or script will fail for you. 
cd ../../../../../../../../../../../../../../etc/ || exit
echo "Current Directory-> $(pwd)"