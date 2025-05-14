'''password rules
1. Minimum 8 characters.
2. The alphabets must be between [a-z]
3. At least one alphabet should be of Upper Case [A-Z]
4. At least 1 number or digit between [0-9].
5. At least 1 character from [ _ or @ or $ ].'''
a = input("Enter the password:")
count = 0
if len(a)>=8:
    for i in a:
        if i.isdigit():
            count = count +1
            break
        elif i.isalpha():
            count = count +1
            break
        elif i.isupper():
            count = count +1
        elif('_','$','@') in a:
             count = count +1
             break
if count == 4:
    print('valid password')
else:
    print("Invalid password")

   
