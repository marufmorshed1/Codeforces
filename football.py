b, a = input().split()
for i in range(1000000000):
    if (i * int(b)) / 2 >= int(a):
        print(i)
        break
    else:
        continue
