#!/usr/bin/python
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
#
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import sys

i, square, sum  = 0,0,0
while i <= 100:
	square += i**2
	sum = sum + i
	i += 1

print sum**2 - square
