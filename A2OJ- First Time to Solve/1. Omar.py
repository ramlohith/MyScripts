#!/usr/bin/python

print "Enter number:"
n=int(raw_input())
c=[]
for i in range(0,n):
  a,b = raw_input().split()
  a = int(a)
  b = int(b)
  c.append(a+b)

for i in c:
  print i
