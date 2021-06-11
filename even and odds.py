n, k = input().split()
m = []

i = 1
j = 1

while i <= int(n):
    if i % 2 != 0:
        m.append(i)
    i += 1

while j <= int(n):
    if j % 2 == 0:
        m.append(j)
    j += 1

print(m[int(k) - 1])
