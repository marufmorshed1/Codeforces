str = input()

str = str.lower()

vow = "aeiouy"

out = ""

for i in str:
    if i in vow:
        continue
    else:
        out = out + "." + i

print(out)