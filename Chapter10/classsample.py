'''
class Sample:
    a = "Harry"

obj = Sample()
obj.a = "VICKY"

print(Sample.a)
print(obj.a)
'''

#Create user by using classsample:
'''
class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")

    def squareRoot(self):
        print(f"The value of {self.number} squareRoot is {self.number **0.5}")


    def cube(self):
        print(f"The value of {self.number} cube is {self.number **3}")

    @staticmethod
    def greet():
        print("****Hello there welcome to the best calculator of the world*****")


a = Calculator(8)
a.greet()
a.square()
a.squareRoot()
a.cube()
'''
'''
class Calcy:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2


    def Sum(self):
        print(f"The sum of both number is:{self.num1+self.num2}")
    def Multi(self):
        print(f"The Multiplication of Number : {self.num1*self.num2}")

b = Calcy(23,32)
b.Sum()
c = Calcy(2,3)
c.Multi()
'''
#Write a class train which has methods to book ticket:
'''
class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is: {self.name}")
        print(f"The seats available in the train are:{self.seats}")

    def fareInfo(self):
        print(f"The price of the ticket is Rs:{self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your Ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1

        else:
            print("Sorry, This train is full! kindly try after sometime")

    def cancelTicket(self):
        if(self.seats>=0):
            print(f"Your ticket has been cancelled!")
            self.seats = self.seats + 1

        else:
            print(f"Ticket will not added in list")


intercity = Train("Intercity Express=14015", 90, 2)
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()
#intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
#intercity.getStatus()
intercity.cancelTicket()
#intercity.getStatus()
#intercity.cancelTicket()
intercity.bookTicket()
'''
class Theatre:
    def __init__(self,name,seat,fare):
        self.name=name
        self.seat=seat
        self.fare=fare
    def getStatus(self):
        print(f"Theatre Name is : {self.name}")
        print(f"Availablity of Seat is:{self.seat}")
        print(f"Fare per seat is: {self.fare}")

    def SeatBooking(self):
        how = int(input(f"Enter number of seats : "))
        if(self.seat>0):
            print(f"Your seat is booked Successfully,Your seat Number is {self.seat,self.seat-(how-1)}")

            self.seat =self.seat - how
        else:
            print("No ticket Available")

    def cancelTicket(self):
        if ( self.seat>= 0):
            print(f"Your ticket has been cancelled!")
            self.seat = self.seat + 1
        else:
            print(f"Ticket will not added in list")

Record = Theatre("Maratha",20,40)
Record.getStatus()
Record.SeatBooking()
Record.cancelTicket()