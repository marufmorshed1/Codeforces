k, n, w = input().split()
price = 0
u = 0
i = 1
while i <= int(w):
    u = i * int(k)
    price = price + u
    i += 1

if price > int(n):
    print(price - int(n))
elif price < int(n) or price == int(n):
    print("0")
