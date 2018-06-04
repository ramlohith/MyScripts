#!/usr/bin/python

import sys

n,t = map(int,raw_input().split())

q = []
q = raw_input()
q = list(q)

for i in range(0,t):
	j = 0
	while j < n:
		if q[j] == 'G' and j-1>=0 and q[j-1] == 'B':
			q[j-1], q[j] = q[j], q[j-1]
			j = j + 2
		else:
			j = j+1

for i in range(0,n):
	sys.stdout.write(q[i]) 
