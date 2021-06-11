a = int(input())
b = int(input())
c = int(input())

w = (a+b)*c
x = a+b*c
y = a*(b+c)
z = a*b*c
m = a+b+c


max = w

if x > max:
    max = x
if y > max:
    max = y
if z > max:
    max = z
if m > max:
    max = m

print(max)