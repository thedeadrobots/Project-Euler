#! /usr/bin/python

import sys

total = 0
def fib(n):
	if n == 0 or n == 1:
		return n
	else:
		return fib(n - 1) + fib(n - 2);

for i in range(34):
	print i
	k = fib(i)
	if k % 2 == 0:
		total = total + k
	
print total
