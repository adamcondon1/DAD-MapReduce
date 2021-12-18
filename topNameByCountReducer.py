#!/usr/bin/env python
import sys

# Initialise a list to store the top N names as a collection of touples (Count, Name)
myList = []
n = 5

for line in sys.stdin:
	# remove whitespace
	line = line.strip()
	# split data values into list
	data = line.split(",")
	
	# convert Count (currently a string) to int
	try:
		Count = float(data[3])
	except ValueError:

		continue
	
	
	# add (count, name) to list
	myList.append( (Count, line) )
	
	# sort list in reverse order
	myList.sort(reverse=True)
	
	# keep only first N name
	if len(myList) > n:
		myList = myList[:n]
	
# Print top N names
for (k,v) in myList:
	print(v)