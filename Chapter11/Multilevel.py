#Multilevel Inheritance:Is one type of inheritance being used to inherit both base class features to
#the newly derived class when we inherit a derived classs from a base classs and another derived
#class from the previous derived class up to any extent of depth of classes in python is called

class Person:
    country = "India"

    def takeBreath(self):
        print("I am Breathing....")

class Employee(Person):
    company = "Honda"
    salary = 20000

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am an Employee so I am luckily breathing...")

class Programmer(Employee):
    company = "Fiver"

    def getSalary(self):
        print("No Salary to Programmer")

    def takeBreath(self):
        print("I am a Programmer so i am breathing.....")


p = Person()
p.takeBreath()
e = Employee()
e.getSalary()
e.takeBreath()
Pr = Programmer()
Pr.getSalary()
Pr.takeBreath()
#print(p.company)#Throw an Error
print(Pr.company)
print(e.company)
print(Pr.country)