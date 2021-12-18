#!/usr/bin/env python
import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove whitespace
    line = line.strip()
    # remove all characters except letters and spaces
    line = re.sub(r'[^a-zA-Z ]', '', line)
    # convert to lowercase
    line = line.lower()
    # split line into words
    words = line.split()
    
    # iterate through all the words
    for word in words:
        # writing the results to STDOUT (standard output);
        print('%s\t%s' % (word, 1))
