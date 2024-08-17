#Python File Operation:
'''File handling is an important part of any web application.
Python has several functions for creating, reading, updating and deleting files.
'''
'''
#Creating a file using python:
file = open('file.txt', 'w')
file.write("This is Mahesh and we are using python."
           "Now we want to check this file created in defined path location or not")
file.close()


#Created file read by using this program
file = open('file.txt', 'r')
print(file.read())


'''
#OOP(Object Oriented Programming) in Python:
#Class and Object in python OOP's:
class person:
    def __init__(self, name, age, city, job, Vehicle):
        self.name = name
        self.age = age
        self.city = city
        self.job = job
        self.Vehicle = Vehicle

mahesh = person("Mahesh", 23, "Mumbai", "Engineer", "Shine")
#a = str(input("Enter name : "))
#b = int(input("Enter age : "))
#c = str(input("Enter City: "))
#d = str(input("Enter Profile: "))
#e = str(input("Enter Vehicle: "))
#mahesh = person(a, b, c, d, e)

print("The person name is", mahesh.name)
print("The person age is", mahesh.age)
print("The city is", mahesh.city)
print("The Person Job is", mahesh.job)
print("The Person Vehicle is", mahesh.Vehicle)
