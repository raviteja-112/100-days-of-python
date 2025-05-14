class employee:
    company = 'microsoft'
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def getdetails(self):
        print(self.name)
        print(self.company)
        print('\n')
n = int(input("Enter the number of employees:"))
l =[]
s = []
for i in range(n):
    a = input('Enter the name :')
    l.append(a)
    b = input('Enter the salary :')
    s.append(b)
for i in range(len(l)):
    l[i] = employee(l[i],b[i])
    l[i].getdetails()


