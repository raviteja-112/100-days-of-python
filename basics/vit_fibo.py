n = int(input('number:'))
a = 0
b = 1
s = 0
for i in range(0,n):
    print(s)
    a = b
    b = s
    s = a+b