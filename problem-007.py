#! /usr/bin/python

import sys
import math

def is_prime(num):
	for p in range(2, int(math.sqrt(num)+1)):
		if num % p == 0:
			return False

primes = []

i = 2 
while i < (2**17):
			
	if is_prime(i) == None:
				primes.append(i)
	i += 1
	if len(primes) == 10001:
		print "10001st prime: ", max(primes)
		break


