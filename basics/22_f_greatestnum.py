def greatest(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            max = n1
        else:
            max = n3
    else:
        if n2>n3:
            max = n2
        else:
            max = n3
    great = max
    return great
    
n1 = int(input("Enter the number 1  :"))
n2 = int(input("Enter the number 2 :"))
n3 = int(input("Enter the number 3 :"))
print(f"The maximum number in {n1,n2,n3} is: ",greatest(n1, n2, n3))
