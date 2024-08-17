'''class Employee:
    company = "Google"
    def getSalary(self):
        print("salary is 100k")

harry = Employee()
harry.getSalary()
#Employee.getSalary(harry)'''

class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The Time is 9AM in the Morning")

harry = Employee()
harry.salary = 100000
harry.getSalary("Thanks!") #Employee.getSalary(harry)
harry.greet() #Employee.greet()
harry.time()