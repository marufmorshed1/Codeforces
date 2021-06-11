str = input()
c = 0
for i in str:
    if 48 <= ord(i) <= 57:
        c += 1


print(c)
