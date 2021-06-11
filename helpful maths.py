s = input()
i = 0
j = 0
l = []
for i in s:
    l.append(i)


while i < len(s):
    while j < (len(s) - 1):
        if int(l[j]) > int(l[j + 2]):
            temp = l[j]
            l[j] = l[j + 2]
            l[j + 2] = temp
    j += 2
i += 2

print(l)
