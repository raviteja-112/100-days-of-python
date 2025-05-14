a = input("Enter the string:")
count1 = 0
count2 = 0
for i in a:
    if i.isupper():
        count1 = count1 +1
    if i.islower():
        count2 = count2+1
print(f"The number of uppercase are {count1} and number of lowercase are {count2}")