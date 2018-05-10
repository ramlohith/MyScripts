#!/usr/bin/python
import sys

n = int(raw_input())
s = 1
while n > 0:
	print " "*(n-1),
	for i in range(s):
		sys.stdout.write('*')
	print"\n"
	s=s+2
	n=n-1

