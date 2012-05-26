#!/usr/bin/python

import sys

x = []
sum_num = 0

for i in range(0, 99):
	x = [line.strip() for line in open('problem-013.txt')]

for i in range (0,100):
	sum_num += int(x[i])
print str(sum_num)[:10]

