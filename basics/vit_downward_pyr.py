n = int(input("Enter any number :"))
for i in range(n):
    for j in range(i,n):
        print("*",end = " ")
        j = j+1
    print("")
    i = i +1    