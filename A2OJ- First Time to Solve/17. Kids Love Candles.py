#!/usr/bin/python

t = int(raw_input( "Enter the number of test cases:"))
n=[]
x=[]

for i in range(t):
	op = 0
	a,b=raw_input().split()
	a=int(a)
	b=int(b)
	n=raw_input()
	n=[int(j) for j in n.split()]
	for k in n:
		op = op + k/b
	x.append(op)
for i in x:
	print i





