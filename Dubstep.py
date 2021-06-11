st = input()
i = 0
x = ""
sl = ""
while i <= (len(st)-3):
    sl = st[i:i+3]
    if sl == "WUB":
        continue
    else:
        x = x + sl + " "
    i += 3


x = x[:-1]

print(x)
