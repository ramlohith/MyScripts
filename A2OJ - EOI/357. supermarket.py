#!/usr/bin/python

l=[]
sum = 0.0
l = map(float,raw_input().split())
for i in range(2,len(l)):
	sum = sum + l[i]

if sum <= l[1]:
	print "Yes"
elif sum > l[1]:
	print "No"
