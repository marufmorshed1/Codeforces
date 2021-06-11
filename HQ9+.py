x = input()

code = "HQ9"
flag = 0

for i in x:
    if i in code:
        flag = 1
        break

if flag == 0:
    print("NO")
else:
    print("YES")
