#!/usr/bin/env python
import sys
 
# Initialise a list to store the top N names as a collection
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
	
	# add (Count, Name)
	if (data[0] in 'A' or 'B' or 'C' or 'D'or 'E' or 'F'or 'G' or 'H'or 'I' or 'J' or 'K' or 'L' or 'M' or 'N' or 'O' or 'P' or 'Q' or 'S' or 'T' or 'U' or 'V' or 'W' or 'X' or 'Y'or'B'): 
		myList.append( (Count, line) )
	
	# sort list in reverse order
	myList.sort(reverse=True)
	
	# keep only first N names
	if len(myList) > n:
		myList = myList[:n]
	
	# Print top N names
	for (k,v) in myList:
		print(v)