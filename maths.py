a, b = input().split()
a = int(a)
b = int(b)

for i in range(b):
    if a % 10 == 0:
        a = int(a)/10
    else:
        a = int(a) - 1
a = int(a)
print(a)