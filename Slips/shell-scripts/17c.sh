#!/bin/sh

# List all the directories except . and .. 

# find . -type d -not \( -name '.' -or -name '..' \)

# ALTERNATE
# ls -A 

# ALTERNATE 2
ls --almost-all