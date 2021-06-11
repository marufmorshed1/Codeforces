a, b = input().split()
a = int(a)
b = int(b)
c = []
d = 0
c = input().split()
for i in c:
    if int(i) > 0 and int(i) >= int(c[b-1]):
        d += 1

print(d)