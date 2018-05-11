a = [[0 for i in range(2)] for j in range(30)]
n = int(raw_input())

for k in range(n):
	a[k] = map(int,raw_input().split())
x = 0

for i in range(n):
	y = a[i][1]
	for j in range(n):
		if y == a[j][0]:
			x = x+1
print x