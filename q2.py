word = input()

a = "EZK"
c = 0
c2 = 0
w = ""
w2 = ""
for i in word:
    if i is "E" or i is "Z" or i is "K":
        while i in word:
            if i is "E" or i is "Z" or i is "K":
                w = w + i
                c = +1
            else:
                break
        i += 1
    else:
        continue

    if c > c2:
        c2 = c
        w2 = w



print(w2)
print(w)
