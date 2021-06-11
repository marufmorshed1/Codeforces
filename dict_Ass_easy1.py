my_dict = {}

my_dict = input().split(',')

i = ""
while i == "Stop":
    i = input()
    j = int(i) in my_dict.values()
    print(j)
    i += 1
