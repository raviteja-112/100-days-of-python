a = input("Enter the string:")
count1 = 0
count2 = 0
for i in a:
    if i.isalpha():
        count1 = count1 +1
    if i.isdigit():
        count2 = count2+1
print(f"The number of digits are {count2} and number of alphabets are {count1}")
