#!/usr/bin/python

#What is the smallest positive number that is evenly divisible by all of the numbers from #1 to 20?

import sys
i = 0
while i < 2**32:
	cnt = 0
	for d in range(1, 20):
		if i % d == 0:
			cnt += 1
		if cnt == 19:
			print "Largest # divisible by 1-20: ", i
			break
	i += 2
