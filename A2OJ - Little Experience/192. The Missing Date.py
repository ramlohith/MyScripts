
print "Enter number of testcases:"
t = int(raw_input())
result=[]

def addmonths(y1,y2,m1,m2):
	m3 = m1+m2
	if (m3 >= 12):
		if(m3%12 == 0):
			result.append((y1+y2+(m3/12)-1,12))
		else:
			result.append((y1+y2+(m3/12),m3%12))
	else:
		result.append((y1+y2,m3))

for i in range(t):
	y1,m1=raw_input().split()
	y1 = int(y1)
	m1 = int(m1)
	y2,m2 = raw_input().split()
	y2 = int(y2)
	m2 = int(m2)
	addmonths(y1,y2,m1,m2)

for j,k in result:
	print str(j) + " " + str(k)
	