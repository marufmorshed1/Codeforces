p = input()

if p[0].isupper():
    print(p)
else:
    print((p[0].upper()) + p[1:len(p)])
