n = int(input())
c = 0
if n <= 5:
    print("1")
elif n % 5 == 0:
    c = n//5
    print(c)
else:
    c = (n//5) + 1
    print(c)

