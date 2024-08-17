'''
class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit, city):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        self.city = city
        print("Employee is Created!")


    def getDetails(self):
        print(f"The name of Employee is {self.name},salary of the employee is {self.salary},"
              f"subunit of employee is {self.subunit},The City of Employee is {self.city}")
        #print(f"The name of Employee is {self.name}")
        #print(f"The salary of the employee is {self.salary}")
        #print(f"The subunit of employee is {self.subunit}")
        #print(f"The City of Employee is {self.city}")

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The Time is 9AM in the Morning")

harry = Employee("Harry", 100, "Youtube", "Mumbai")
mahesh = Employee("Mahesh", 200, "Chrome", "Pune")
vijay = Employee("Vijay", 300, "Vidmate", "Bengaluru")
g = mahesh.greet()
t = mahesh.time()
#harry.getDetails()
mahesh.getDetails()
#mahesh.getSalary()
#vijay.getDetails()
'''
class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit, city):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        self.city = city
        print("Employee is Created!!")


    def getDetails(self):
        print(f"The name of Employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of employee is {self.subunit}")
        print(f"The City of Employee is {self.city}")

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The Time is 9AM in the Morning")

harry = Employee("Harry", 100, "Youtube", "Mumbai")
mahesh = Employee("Mahesh", 200, "Chrome", "Pune")
vijay = Employee("Vijay", 300, "Vidmate", "Bengaluru")

#harry.getDetails()
mahesh.getDetails()
#vijay.getDetails()