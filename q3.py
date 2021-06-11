def totalCost(*x):
    prod = x[0]
    i = 1
    sum = 0
    while i <= (len(x)-1):
        prod = prod * int(x[i])
        sum = sum + prod
        i += 1
    print(sum)


totalCost(3,6,2,9)