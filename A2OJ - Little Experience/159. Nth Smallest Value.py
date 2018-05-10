#!/usr/bin/python

print "Enter the number of test cases:"
t=int(raw_input())
x=[]
y=[]

for i in range(t):
	x = raw_input().split()
	x = [int(k) for k in x]
	x.sort()
	y.append(x[1])

for j in y:
	print j

