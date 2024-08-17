#Make a programm which store programmer list:

class Programmer:
    compmany = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of Programmer is {self.name} and the product is {self.product}")

harry = Programmer("Harry", "Skype")
mahesh = Programmer("Mahesh", "Github")
harry.getInfo()
mahesh.getInfo()


'''
#Calculator to square:
class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")

    def squareRoot(self):
        print(f"The value of {self.number} squareRoot is {self.number **0.5}")


    def cube(self):
        print(f"The value of {self.number} cube is {self.number **3}")

a = Calculator(9)
a.square()
a.squareRoot()
a.cube()
'''