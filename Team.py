n = int(input())
s = 0

for i in range(0, n):
    x = input()
    if x.count("1") >= 2:
        s += 1

print(s)
