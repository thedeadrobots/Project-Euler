#! /usr/bin/python

import sys
import math

def is_prime(pot_factor):
	for p in range(2, int(math.sqrt(pot_factor)+1)):
		if pot_factor % p == 0:
			print "not a prime factor: ", pot_factor, " / ", p
			return False

x = 600851475143
#x = 13198
primes = []

pot_factor = 1
while pot_factor < (int(math.sqrt(x)+1)):
	if x % pot_factor == 0: #if its a factor
		print "potential factor: ", pot_factor, " multiplier: ", x/pot_factor
		if pot_factor % 2 != 0: #if factor is not even, pot prime
			if is_prime(pot_factor) == None:
				primes.append(pot_factor)
	pot_factor += 1

print primes
print "largest prime is ", max(primes)
