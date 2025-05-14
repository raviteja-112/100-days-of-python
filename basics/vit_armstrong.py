n = int(input("Enter any number :"))
n1 = n
temp = n
i = 0
while n > 0:
    n = n//10
    i = i+1
sum = 0 
while n1 > 0:
    dig = n1 % 10
    sum = sum + dig**i
    n1 = n1 //10
if temp == sum:
    print("it is a armstrong number ")
else:
    print("it is not a armstrong number ")     

