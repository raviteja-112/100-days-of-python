#not finialized
n = int(input("Enter how many numbers you want:"))
i = 1
a = 1 
while i<=n:
    j = 1
    count = 0
    while j<=a:
        if a % j == 0:
            count = count +1
        j = j+1 
    if count == 2:
        print(a)
        a = a+1  
    i = i+1
      
