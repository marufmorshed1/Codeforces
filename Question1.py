word = input()

cCount = 0
for i in word:
    if 65 <= ord(i) <= 90:
        cCount = cCount + 1

cCount = str(cCount)
print("Number of capital letters: " + cCount)
