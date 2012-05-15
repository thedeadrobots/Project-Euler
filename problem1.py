#!/usr/bin/python
total = 0
for i in range (1,1000): 
	if i % 3 == 0:	total += i 
	elif i % 5 == 0: total += i
print "final count is",  total

