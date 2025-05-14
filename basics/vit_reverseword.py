a = input("Enter the sentence :")
b = a.split()
c = []
for word in b:
    c.append(word[::-1])
#for i in c:
#    print(i,end=' ')
print(' '.join(c))



