#!/usr/bin/python

# What is the value of the first triangle number to have over five hundred divisors?

import sys
import math
import datetime

t = datetime.datetime.now()
answer= []
count_check = []
triangles = [1]

for i in range(2, 15000):
	triangles.append((max(triangles)+i))
	number = max(triangles)
	cnt = 0
	for j in range(1, int(math.sqrt(max(triangles)))):
			if number % j == 0:
				cnt += 1
			if cnt > 250:
				answer.append(number)

print min(answer)
print "run time: ", datetime.datetime.now() - t
