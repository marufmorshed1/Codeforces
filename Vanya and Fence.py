n, h = input().split()
x = input().split()

g = 0
while g < len(x):
    temp = int(x[g])
    x[g] = temp
    g += 1

n = int(n)
h = int(h)

c = n

for i in x:
    if i > h:
        c += 1


print(c)