n = int(input("Enter any number :"))
i = 2
flag = True
while i < n:
    if n%i == 0:
        flag = False
        break
    i = i+1    
if flag == True:
    print("Prime number ")
else:
    while i<n:
        if n % i == 0:
            large = i
        i = i+1
    small = n / large 
    print("The largest divisor is :",large)
    print("The smallest divisor is :",small)        