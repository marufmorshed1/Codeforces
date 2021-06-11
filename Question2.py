def palindromeCheck(x):
    word = x.split()
    temp = ""

    for i in word:
        temp = temp + i

    if temp == temp[::-1]:
        print("true")
    else:
        print('false')


palindromeCheck("nurses run")