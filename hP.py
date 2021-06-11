a, b = input().split()
c = 0
for i in range(100):
    if int(a) > int(b):
        print(c)
        break
    else:
        a = int(a) * 3
        b = int(b) * 2
        c = int(c) + 1
