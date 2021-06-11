list = input().split(",")
sList = []
temp = ""
l=len(list)
for i in range(l):
    if 65 <= ord(i) <= 90:
        for j in range((i + 2), l):
            if list[i] > list[j]:
                l1 = list[i]
                list[i] = list[j]
                list[j] = l1
                l2 = list[i+1]
                list[i+1]=list[i+3]
                list[i+3]=l2
print(list)