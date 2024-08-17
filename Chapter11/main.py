#INHERITANCE AND MORE ON OOPS:Inheritance is concept in oop where existing
#When a class inherits some or all of the behaviors from another class is known as Inheritance.
#classes can be modified by a new classes.
'''
class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"
    company = "Youtube"

    def getlanguage(self):
        print(f"The language is {self.language()}")

    def showDetails(self):
        print("This is a Programmer")

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)
print(e.company)
'''

#Types of Inheritance:1)Single 2)Multiple 3)Multilevel
#Single Inheritance:(Above Example) a derived class is derived only from a single parent class
#Multiple Inheritance:(2Parent 1child)When class is derived from more than one base class

class Employee:
    company = "visa"
    eCode = 120
    level = 0

    def upgradelevel(self):
        self.level = self.level + 1

class Freelancer:
    company ="Fiver"

class Programmer(Employee, Freelancer):
    name ="Rohit"

p = Programmer()
p.upgradelevel()
print(p.level)
print(p.company)
print(p.eCode)
print(p.name)