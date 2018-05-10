l = []
sum = 0

while len(l) < 3:
	line = map(int, raw_input().split())
	for i in line:
		l.append(i)
		sum = sum + i

print format((sum * 2), '.6f')

