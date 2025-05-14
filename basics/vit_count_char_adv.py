#we are making this to find just characters(num,alpha) not special char
a = input("Enter the string:")
count = 0
for i in a:
    if (i.isalpha() or i.isdigit()):
        count = count+1
print('the number of character are :',count)