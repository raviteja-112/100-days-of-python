l = []
l1 = []
n = int(input("Enter the number of elements you want :"))
for i in range(n):
    a = (int(input("Enter a number: ")))
    l.append(a)
for i in l:
    if (i % 2) == 0:
        l1.append(i)
print(l1)