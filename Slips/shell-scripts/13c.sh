#!/bin/sh

# Create a 0-byte file and change the permissions of a file to “rwxr-x—x” while displaying what changes were exactly made to current permissions.

touch 0bytefile
chmod u=rwx,g=rx,o=x 0bytefile
ls -l 0bytefile
