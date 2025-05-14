n = int(input("Enter the number :"))
i = 0
sum = 0
while n>0:
    dig = n%10
    sum = sum + dig
    n = n//10
    i = i+1
    
print(sum)    
    