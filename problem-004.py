#!/usr/bin/python

import sys

palindromes = []
#assumption: palindrome exists in the last hundred 3 digit numbers.
for i in range (900, 999):
	for j in range(900, 999):
		product = i * j
		if str(product) == str(product)[::-1]:
			palindromes.append(product)

print palindromes

