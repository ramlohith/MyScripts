s = raw_input()
s = list(s)
x = []

if s.count('h') >= 1 or s.count('e') >= 1 or s.count('l') >= 2 or s.count('o') >=1:
	for i in s:
		if not x:
			if i == 'h':
				x.append(i)
			else:
				continue
		elif len(x) == 1:
			if i == 'e':
				x.append(i)
			else:
				continue
		elif len(x) == 2:
			if i == 'l':
				x.append(i)
			else:
				continue
		elif len(x) == 3:
			if i == 'l':
				x.append(i)
			else:
				continue
		elif len(x) == 4:
			if i == 'o':
				x.append(i)
			else:
				continue
		else:
			continue
else:
	print "NO"

x = ''.join(x)
if(x.find('hello') > -1):
	print "YES"
else:
	print "NO"