#!/usr/bin/python

import sys

f = open('problem-011.txt', 'r')
x = []
answer = 0
for i in range(0, 20): 
	x.append([])
	for j in range(0, 20):
		x[i].append(int(f.read(3)))

for i in range(0,16):
	for j in range(0,16):
	  #horiz
		product = []
		product.append(x[i][j] * x[i][j+1] * x[i][j+2] * x[i][j+3])
		#deal with 17,18,19
		product.append(x[i+1][j] * x[i+1][j+1] * x[i+1][j+2] * x[i+1][j+3])
		product.append(x[i+2][j] * x[i+2][j+1] * x[i+2][j+2] * x[i+2][j+3])
		product.append(x[i+3][j] * x[i+3][j+1] * x[i+3][j+2] * x[i+3][j+3])
		
		#vert
		product.append(x[i][j] * x[i+1][j] * x[i+2][j] * x[i+3][j])
		product.append(x[i][j+1] * x[i+1][j+1] * x[i+2][j+1] * x[i+3][j+1])
		product.append(x[i][j+2] * x[i+1][j+2] * x[i+2][j+2] * x[i+3][j+2])
		product.append(x[i][j+3] * x[i+1][j+3]* x[i+2][j+3]* x[i+3][j+3])
	  
			
		product.append(x[i][j] * x[i+1][j+1] * x[i+2][j+2] * x[i+3][j+3])
		product.append(x[i+3][j] * x[i+2][j+1] * x[i+1][j+2] * x[i][j+3])	
	  
		if max(product) > answer:
			answer = max(product)
print answer
