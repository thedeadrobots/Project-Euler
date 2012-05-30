#!/usr/bin/python

import sys
import datetime

t = datetime.datetime.now()
finals = {}

for n in range(1, 1000000):
	chain = []
	starter = n
	while n > 1:
		if n % 2 == 0:
			n = n / 2
			chain.append(n)
		else:
			n = (3*n) + 1
			chain.append(n)
	finals[len(chain)] = starter

#print finals
print "Number: ", finals[max(finals)], " has ",  max(finals), " elements in the sequence" 
print "run time: ", datetime.datetime.now() - t

