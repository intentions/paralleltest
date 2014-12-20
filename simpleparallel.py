#!/usr/bin/python
"""
This program is a test of parallel processing using python
It splits a simple module 2 or 3 check of a series of numbers
one process checks to see what numbers in the list are divisible
by 2 and the other if it is divisible by 3
"""

#imports
from multiprocessing import Pool
import os

def outer(n):
	"""
	this function prints a statement and a number	
	"""
	pid = os.getpid()
	print "a forked process {0}, is running with pid of {1}".format(str(n), str(pid))
	return(n, "done")

def parallelRun(N):
	"""
	takes in a number and creates threads of that number	
	"""

	pool = Pool()
	i = 0
	results = []

	for i in xrange(0, N):
		r = pool.apply_async(outer, [i])
		results.append(r)

	for r in results:
		a, b = r.get()
		print "forked process {0} is {1}".format(str(a), b) 


	return("done")

if __name__ == "__main__":
	"""
	main program
	"""
	parallelRun(2)
	
