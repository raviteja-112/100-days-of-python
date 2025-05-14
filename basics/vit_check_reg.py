a = input("Enter your reg.no:")
a.upper() #we are uppercase thing 
if (len(a)==9):
    for i in a:
        if(a[0:1].isdigit() & a[2:4].isalpha() & a[5:8].isdigit()):
            print("Valid reg")
            break
        else:
            print('Invalid reg')
else:
     print('Invalid reg')
