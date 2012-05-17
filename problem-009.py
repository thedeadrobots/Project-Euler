#!/usr/bin/python

import sys
import math

for i in range(1, 1000):
	for j in range(1, 1000):
		a = i
		b = j
		c = 1000 - (i + j)
		
		if a**2 + b**2 == c**2:
			print a, b, c
			print a * b * c


