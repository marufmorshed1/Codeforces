y = int(input())

flag = 0
y += 1
x = ''

while flag == 0:
    x = str(y)
    if x[0] != x[1] and x[1] != x[2] and x[2] != x[3] and x[3] != x[0] and x[0] != x[2] and x[1] != x[3]:
        flag = 1
        break
    else:
        y += 1

print(x)