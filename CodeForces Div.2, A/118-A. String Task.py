#!/usr/bin/python

import string
import sys

s = raw_input()
l = []

for i in range(0,len(s)):
	if s[i] in ('a','e','i','o','u','y','A','E','I','O','U','Y'):
		continue
	elif (s[i].isupper()):
		a = s[i].lower()
		l.append(a)
	else:
		l.append(s[i])

l = [v for j in l for v in ('.',j)]
for i in l:
	sys.stdout.write(i)
