class calc:
    @staticmethod
    def greet():
        print('Welcome to the calculator')
    def __init__(self,n):
        self.n = n 
    def square(self):
        print((self.n)**2)
    def cube(self):
        print((self.n)**3)
    def squarer(self):
        print((self.n)**0.5)
n = int(input('Enter the number:'))
v = calc(n)
v.greet()
v.square()
v.cube()
v.squarer()