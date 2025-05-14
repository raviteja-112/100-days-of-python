a = int(input("ENter the number "))
prime = True #we assumed that it prime
for i in range(2,a):
    if a % i == 0: #if it is completly divided by then it is not a prime number 
        prime = False
        break
if prime == True:
    print("prime")
else:
    print("non prime")      