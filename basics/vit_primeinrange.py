for i in range(10,101):
    a = 0
    for j in range(2,i):
        if i%j == 0:
            a = a+1
    if a == 0:
        print(i)
