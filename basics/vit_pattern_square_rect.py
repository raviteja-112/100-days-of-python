n = int(input("Enter the number :"))
for i in range(n): #this is for rows 
    for j in range(n): #this is for columns
        print("*",end = " ")
        j = j + 1
    print("\n")
    i = i+1       