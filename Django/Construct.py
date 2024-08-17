#Inheritence
'''class Employee:
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender

    def show_employee_details(self):

        print("Name of Employee is:",self.name)
        print("Age of Employee is:",self.age)
        print("Salary of Employee is:",self.salary)
        print("Gender of Employee is:", self.gender)

e1= Employee("Vijay",23,2000,"Male")
e2= Employee("Suraj",22,3200,"Male")

e1.show_employee_details()
e2.show_employee_details()'''
'''
#PARENTS CLASS:
class vehicle:
    def __init__(self,mileage,cost,condition):
        self.mileage=mileage
        self.cost=cost
        self.condition=condition

    def show_vehicle_details(self):
        print("I am a vehicle")
        print("Mileage of vehicle is:",self.mileage)
        print("Cost of vehicle is:",self.cost)
        print("Condition of vehicle is:",self.condition)

v1=vehicle(300,5000)
v1.show_vehicle_details()
v2=vehicle(200,3200)
v2.show_vehicle_details()'''#for child program this can be removed
'''
#CHILD CLASS:
class car(vehicle):
    def show_vehicle_details(self):
        print("I am Car")
        print("Mileage of vehicle is:",self.mileage)
        print("Cost of vehicle is:",self.cost)
        print("Condition of my car is:",self.condition)

c1 = car(100,4000,"Good")
c1.show_vehicle_details()
'''


#Single inheritance example:
class vehicle:
    def __init__(self,m,c):
        self.mileage=m
        self.cost=c

    def show_vehicle_details(self):
        print("I am a vehicle")
        print("Mileage of vehicle is:", self.mileage)
        print("Cost of vehicle is:", self.cost)

class car(vehicle):
    def __init__(self,m,c,t,h):

        super().__init__(m,c)
        self.tyre=t
        self.hp=h
    def show_car_details(self):
        print("I am a car")
        print("Number of tyres:",self.tyre)
        print("Value of hp is:",self.hp)


c1=car(30,3000,4,500)
c1.show_vehicle_details()
c1.show_car_details()