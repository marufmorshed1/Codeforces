s = input()
q = "helo"
r = ""
for i in s:
    if i in r:
        continue
    else:
        r = r + i

if q in r:
    print("YES")
else:
    print("NO")