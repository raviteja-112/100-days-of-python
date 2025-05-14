a = {'a':3,'b':4,'g':5,'t':6,'y':1,'u':5}
b = a.copy()
for i in a:
    if a[i] % 2 != 0:
        b.pop(i)
print(b)

