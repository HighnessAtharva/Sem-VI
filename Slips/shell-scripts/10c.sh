#!/bin/sh

# Try changing permissions of a non-existent file but the command output shouldn’t show any error message at all.      

# chmod 777 /tmp/xyz 2> /dev/null

# ALTERNATE SOLUTION:

chmod 777 fake.c --quiet