n = int(input("Enter the number you want to check:"))
prime = True
for i in range(2,n):
    if (n%i == 0):
        prime = False
        break
if prime == True: #not required  == True we can write (prime)
    print(f'This number {n} is prime')
else:
    print(f"This number {n} is not prime")