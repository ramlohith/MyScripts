#!/usr/bin/python
import sys

a = int(raw_input())

for i in range (a):
	for j in range(i+1):
		sys.stdout.write('*')
	sys.stdout.write('\n')

