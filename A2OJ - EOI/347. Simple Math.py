import math

a,b,c = map(float, raw_input().split())

d = b ** 2 - (4 * a * c)
x = ((-1 * b) + math.sqrt(d)) /(2 * a)

print format(x,'.6f')