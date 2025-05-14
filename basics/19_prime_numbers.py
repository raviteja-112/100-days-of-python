n = int(input("Enter the number you want to check:"))
count = 0
for i in range(1,n):
    if n%i == 0:
        count = count +1
if (count == 1):
    print(f"The number {n} is a prime number")
else:
    print(f"The number {n} is not a prime number ")
