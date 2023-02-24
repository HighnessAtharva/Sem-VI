#!/bin/sh

# Try changing permissions of a non-existent file but the command output shouldn’t show any error message at all.      

# here 2> means redirecting the error message to /dev/null. >2 is used for error redirection
chmod 777 /tmp/xyz 2> /dev/null

# ALTERNATE SOLUTION:

chmod 777 fake.c --quiet