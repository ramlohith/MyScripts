import sys

n = int(raw_input())
a = []
a = map(int,raw_input().split())
op = []

for i in range(0,n):
	op.insert(i,a.index(i+1))

for i in op:
	print i+1,