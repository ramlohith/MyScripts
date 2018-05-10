#!/usr/bin/python

print "Enter the number of Test Cases:"
T = int(raw_input())
result = []
for i in range(T):
	n,x,y = [int(p) for p in raw_input().split()]
	balloons = raw_input().split()
	balloons = [int(k) for k in balloons]
	if (balloons[0] == x and balloons[-1] == y): 
		result.append('BOTH')
	elif (balloons[0] !=x and balloons[-1] == y):
		result.append('HARD')
	elif (balloons[0] == x and balloons[-1] != y):
		result.append('EASY')
	else:
		result.append('OKAY')

for i in result:
	print i

