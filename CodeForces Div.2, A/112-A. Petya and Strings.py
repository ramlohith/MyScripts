#!/usr/bin/python

import string 

a = str(raw_input())
b = str(raw_input())

a = a.lower()
print a
b = b.lower()
print b

if a < b:
	print "-1"
elif a> b:
	print "1"
elif a == b:
	print "0"

