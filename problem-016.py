import sys

a = list(str(2**1000));
sum = 0

for i in range(0, len(a)):
	sum += int(a[i])

print sum
