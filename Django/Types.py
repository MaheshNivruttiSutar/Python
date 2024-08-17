#Multiple Inheritance in Python
'''class parent1:
    def assign_str_one(self,str1):
        self.str1=str1

    def show_str_one(self):
        print("string one is",self.str1)

class parent2:
    def assign_str_two(self,str2):
        self.str2=str2

    def show_str_two(self):
        print("string two is:",self.str2)

class child(parent1,parent2):
    def ass_str_three(self,str3):
        self.str3=str3

    def show_str_three(self):
        print("string three is:",self.str3)

c1=child()
c1.assign_str_one("one")
c1.assign_str_two("two")
c1.ass_str_three("three")

c1.show_str_one()
c1.show_str_two()
c1.show_str_three()'''

#Parennts,Child and Grandchild:
class parent:
    def assign_name(self,name):
     self.name=name

    def show_name(self):
         print("Name is :",self.name)

class child(parent):
    def assign_age(self,age):
     self.age=age

    def show_age(self):
        print("Age is :",self.age)

class grandchild(child):
    def assign_gender(self,gender):
        self.gender=gender

    def show_gender(self):
        print("Gender is:",self.gender)

g1 = grandchild()

g1.assign_name("Raj")
g1.assign_age(23)
g1.assign_gender("Male")

g1.show_name()
g1.show_age()
g1.show_gender()