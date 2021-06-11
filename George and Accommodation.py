n = int(input())
counter = 0

i = 0
while i < n:
    a, b = input().split()
    if int(a) + 1 < int(b):
        counter += 1
    i += 1

print(counter)
