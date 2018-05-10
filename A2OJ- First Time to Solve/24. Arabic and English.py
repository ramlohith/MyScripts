#!/usr/bin/python

print "Enter the number of test cases:"
t = int(raw_input())
y = []
for i in range(t):
	w = int(raw_input())
	x = raw_input().split(' ')
	x= list(x)
	a = 0
	for j in x:
		if(j.isalpha()):
			a = a + 1
			ind = x.index(j)
	if (a > 0 and ind != 0):
		b = len(x)-ind
		for p in range(0,b):
			x.insert(p,x[-1])
			x.pop()
	y.append(x)

for i in y:
	print " ".join(i)
