class train:
    def __init__(self,train,seats,fare):
        self.train = train
        self.seats = seats
        self.fare = fare
    def booking(self):
        if (self.seats>0):
            print("you have succesfully booked seat")
            self.seats = self.seats-1
        else:
            print("try again after some time")
    def status(self):
        print(f'There are {self.seats} seats available')
    def fare(self):
        print(f'The fare is rs. {self.fare}')
howarah = train('howrah',45,90)
chennai = train('chennai',30,80)
venkata = train('venkata',20,100)
d = {'howrah':1,'chennai':2,'venkata':3}
print('The trains availabe are',list(d.keys()))
## incomplete because to get values from dict.
b = int(input('Enter the train number '))
a = int(input('''press 1 for booking \n press 2 for status \n press 3 for fare'''))
if a == 1:
    howarah.booking()
elif a == 2:
    howarah.status()
elif a == 3:
    howarah.fare()
else:
    print('Invalid input')
    