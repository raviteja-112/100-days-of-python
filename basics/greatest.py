num1 = int(input("Enter the number 1:"))
num2 = int(input("Enter the number 2:"))
num3 = int(input("Enter the number 3:"))
num4 = int(input("Enter the number 4:"))
if (num1>num4):
    c1 = num1
else:
    c1 = num4
if(num2>num3):
    c2 = num2
else:
    c2 = num3
if(c1>c2):
    print('The greatest number is :',c1)
else:
    print('The greatest number is :',c2)
