#!/usr/bin/python
"""
This program is a test of parallel processing using python
It splits a simple module 2 or 3 check of a series of numbers
one process checks to see what numbers in the list are divisible
by 2 and the other if it is divisible by 3
"""

#imports
from multiprocessing import Pool

def modSweep(n, sequence):
	"""
	This function traverses sequence, recording numbers for whom
	the resut number mod sequence value is 0
	"""
	#initialize a blank output list
	output = []

	#traverse sequence, adding number to output when number mod i == 0
	for i in sequence:
		if n % i == 0:
			output.append(i)

	#return output
	return(output)

def parallelRun(numbs, sequence)
	"""
	this function takes two lists of numbers:
	numbs: the pair of numbers to be checked
	sequence: the list of numbers to be checked against
		This list is broken into 
	
	"""

	seq1 = sequence[:len(sequence)/2]
	seq2 = sequence[len(sequence)/2:]
	n1 = numbs[:len(numbs)/2]
	n2 = numbs2[len(numbs)/2:]

	pool = Pool()
	result1 = pool.apply_async(modSweep, [n1, seq1]
	resulti2 = pool.apply_async(modSweep, [n2, seq2]


