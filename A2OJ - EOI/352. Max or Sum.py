a,b,c = map(int,raw_input().split())

if max(a,b,c) > a+b:
	print max(a,b,c)
else:
	print a+b