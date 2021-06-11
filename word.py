n = input()
cl = 0
sl = 0

for i in n:
    if i.isupper():
        cl += 1
    elif i.islower():
        sl += 1


if sl > cl or sl == cl:
    print(n.lower())
else:
    print(n.upper())
