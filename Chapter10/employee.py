class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()

#Creating Instance atttribute salary for both the object
#harry.salary = 300
#rajni.salary = 434

print(harry.company)
print(rajni.company)
Employee.company = "youTube"
print(harry.company)
print(rajni.company)
print(harry.salary)
print(rajni.salary)