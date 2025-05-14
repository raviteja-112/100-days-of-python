#finding the sum of even and odd in range 12 and 37
sum_even = 0
sum_odd = 0
i = 12
while i <= 37 :
    if i % 2 == 0:
        sum_even = sum_even+i 
    else: 
        sum_odd = sum_odd+i
    i = i+1    
print("the sum of the even numbers between 12 and 37 is :",sum_even) 
print("the sum of the odd numbers between 12 and 37 is :",sum_odd)   