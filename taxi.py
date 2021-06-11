n = int(input())

l = input().split()

i = 0
sum = 0
while (i <= n - 1):
    sum = sum + int(l[i])
    i += 1

if sum % 4 == 0:
    j = sum // 4
else:
    j = (sum // 4) + 1
print(j)
