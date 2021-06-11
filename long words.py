n = int(input())

for i in range(0,n):
    w = input()
    l = len(w)

    if l > 10:
        print(w[0], end="")
        print(l-2, end="")
        print(w[l-1])
    else:
        print(w)