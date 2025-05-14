a = {'a':3,'b':4,'g':5,'t':6,'y':1,'u':5}
b = {}
for i in a:
    b.update({a[i]:i})
print(b)