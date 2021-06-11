a = int(input())
b = input()

x = b.count("A")
y = b.count("D")

if x > y:
    print("Anton")
elif y > x:
    print("Danik")
else:
    print("Friendship")
