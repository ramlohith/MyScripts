#!/usr/bin/python

t = int(raw_input())
a=[]

for i in range(t):
	w = raw_input()
	if len(w) > 10:
		x = w[0] + str(len(w) -2) + w[len(w)-1]
		a.append(x)
	else:
		a.append(w)
for i in a:
	print i
