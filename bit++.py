a = int(input())

x = 0

for i in range(a):
    b = str(input())
    if b[1] == '+':
        x += 1
    else:
        x -= 1
print(x)
