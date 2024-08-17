'''class C2dVec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class C3dVec(C2dVec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2d = C2dVec(1, 3)
v3d = C3dVec(1, 9, 7)
print(v2d)
print(v3d)'''


#Make class aniamal and print dog sound:
'''class Animal:
    animalType = "Mammal"

class Pets:
    colour = "White"

class Dog:
    @staticmethod
    def bark():
        print("Bow Bow..!!")

d = Dog()
d.bark()'''


#salaryAfterIncrement:
class Employee:
    salary = 1000
    Increment = 1.5
    @property
    def salaryAfterIncrement(self):
        return self.salary*self.Increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary

e = Employee()
print(e.salaryAfterIncrement)

print(e.Increment)
e.salaryAfterIncrement = 2000
print(e.Increment)
print(e.salaryAfterIncrement)
