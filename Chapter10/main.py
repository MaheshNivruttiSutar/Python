#Object Oriented Programming:
'''
class Number:
    def sum(self):
        return self.a + self.b

num = Number()
num.a = 44
num.b = 30
s = num.sum()
print(s)
'''
'''class Student:
    def TotalStudent(self):
        return self.boys + self.girl
total = Student()
total.girl = 32
total.boys = 40
T = total.TotalStudent()
print(T, "is a Total Student")
'''
'''
class Word:
    def sum(self):
        return self.a + self.b

num = Word()
num.a = 44
num.b = 33
s = num.sum()
print(s)
'''

'''class Number:
    def minus(self):
        return self.a - self.b
num = Number()
num.a = 44
num.b = 33
m = num.minus()
print(m)
'''
'''
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

maheshApplication = RailwayForm()
maheshApplication.name = "Mahesh"
maheshApplication.train = "Rajdhani Express"
maheshApplication.printData()
'''

#Game Programm for Understanding:

class Remote():
    pass

class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveTop(self):
        pass

remote1 = Remote()
player1 = Player()
if(remote1.pressed()):
    player1.moveLeft()