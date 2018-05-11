n=int(raw_input())
a = map(int, raw_input().split())

get_indexes = lambda a,xs:[i for (y,i) in zip(xs,range(len(xs))) if a==y]

x = get_indexes(min(a),a)
y = get_indexes(max(a),a)

if max(x) > min(y) :
	print n-1-max(x) + min(y)
elif max(x) == min(y):
	print "0"
else:
	print n-1-max(x) + min(y) -1
