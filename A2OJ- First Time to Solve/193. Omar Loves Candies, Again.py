#!/usr/bin/python
from collections import Counter

def mysortfun(x):
	return (-x[1],x[0])

x = []
print "Enter the number of test cases:"
t = int(raw_input())
for i in range(t):
	candy = raw_input()
	c = Counter(candy).most_common()
	x.append(sorted(c, key = mysortfun)[0])
for i,j in x:
	print j,i

