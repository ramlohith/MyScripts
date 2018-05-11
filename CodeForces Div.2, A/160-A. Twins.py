#!/usr/bin/python

n = int(raw_input())
a=[]
b=[100]
a = map(int,raw_input().split())
a.sort(reverse=True)
x = a[0]
b[0] = x
a.pop(0)

for i in range(0,len(a)):
	if(sum(b) <= sum(a)):
		b.append(a[0])
		a.pop(0)
	else:
		break
print len(b)


