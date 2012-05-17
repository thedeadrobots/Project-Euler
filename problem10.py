#! /usr/bin/python

import sys
import math

def is_prime(num):
	for p in range(2, int(math.sqrt(num)+1)):
		if num % p == 0:
			return False

prime = 0 

i = 2 
while i < (2000000):
	if is_prime(i) == None:
				prime += i
	i += 1
print prime

