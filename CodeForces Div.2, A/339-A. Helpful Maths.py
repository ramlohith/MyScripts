#!/usr/bin/python

import sys

a = raw_input()
a = list(a)
a.sort()
for i in range(0,(len(a)-1)/2):
	a.pop(0)
a = [v for i in a for v in (i,'+')]
a.pop()
for i in a:
	sys.stdout.write(i)
