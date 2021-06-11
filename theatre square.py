a, b, c = input().split()

if int(a) % int(c) == 0:
    x = int(a)//int(c)
else:
    x = (int(a)//int(c)) + 1

if int(b) % int(c) == 0:
    y = int(b)//int(c)
else:
    y = (int(b)//int(c)) + 1

print(x*y)