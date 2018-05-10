
print "Enter number of test cases:"
t = int(raw_input())
r = list()
for i in range(t):
	s,n,p = raw_input().split()
	s = int(s)
	n = int(n)
	p = int(p)
	
	if ((s-p)%n == 0):
		r.append("YES")		
	else:
		r.append("NO")

for j in r:
	print j