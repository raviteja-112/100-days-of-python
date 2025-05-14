def sum(n):
    if n == 1:
        return 1
    else:
        c = sum(n-1)+n
        return c
n = int(input("Enter the number :"))
print("The sum is :",sum(n))
        
