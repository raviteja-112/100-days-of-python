#finding sum = x+x^2/2+x^3/3+......x^n/n
#with two decimals points
print("Welcome to the program")
n = int(input('Enter the value of n:'))
x = int(input("Enter the value of x:"))
i = 1
sum = 0
while i<=n:
    sum = sum + (x**i)/i
    i = i+1
sum_2 = format(sum,'.2f')
print(sum_2)
