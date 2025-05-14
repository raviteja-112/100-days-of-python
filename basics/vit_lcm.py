a = int(input("Enter the 1 number : "))
b = int(input("Enter the 2 number : "))
if a>b:
    max = a
else:
    max = b
while True:
    if max % a == 0 and max % b == 0:
        break
    max = max+1
print(f"the lcm of {a} and {b} is:",max)        