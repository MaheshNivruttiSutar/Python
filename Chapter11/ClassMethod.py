#Class Method: is a method which is boound to the class and not the object of the class.

'''
class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

    def changeSalary(self, sal):
        self.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)
'''
'''
class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

    #def changeSalary(self, sal):
        #self.salary = sal

    @classmethod
    def changeSalary(self, sal):
        self.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)'''

#Property Decoder:
'''
class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus =400
    totalsalary = 6100

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

e = Employee()
print(e.totalSalary)'''

#Setter & Getter:

class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus =400
    totalsalary = 6100

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary


e = Employee()
print(e.totalSalary)
e.totalSalary = 5800
print(e.salary)
print(e.salarybonus)