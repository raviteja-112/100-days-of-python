a = input("Enter the sentence:")
i = 0
b = ''
while i<len(a):
    if a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u': 
        b = b+ a[i].capitalize()
    else:
        b = b+a[i]
    i = i+1
print(b)