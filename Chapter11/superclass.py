class Person:
    country = "India"

    def __init__(self):
        print("Intilizing Person.....\n")


    def takeBreath(self):
        print("I am Breathing....")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Intilizing Employee.....\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am luckily breathing...")

class Programmer(Employee):
    company = "Fiver"

    def __init__(self):
        super().__init__()
        print("Intilizing Programmer.....\n")


    def getSalary(self):
        print("No Salary to Programmer")

    def takeBreath(self):
        super().takeBreath()
        print("I am a Programmer so i am breathing.....")


#p = Person()
#p.takeBreath()

e = Employee()
#e.takeBreath()

Pr = Programmer()
#Pr.takeBreath()

#print(p.company)#Throw an Error
print(Pr.company)
print(e.company)
print(Pr.country)
