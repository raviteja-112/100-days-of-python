n = int(input("Enter the number :"))
i = 2
count = 0
while n>i:
    if n % i == 0:
        count = count +1
    
    i = i + 1
    

if count  == 0:
    print("prime")
else:
    print("non prime")        
