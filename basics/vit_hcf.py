a = int(input("Enter the 1 number :"))
b = int(input("Enter the 2 number:"))
if a>b:
    min = b
else:
    min = a
i = 1
while i<=min:
    if a%i == 0 and b % i ==0:
        hcf = i 
    i = i + 1    
print(hcf)        