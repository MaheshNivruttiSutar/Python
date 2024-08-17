#Function
'''
#This code is used sum formula:
marks = [45, 78, 86,77]
Percentage1 = ((sum(marks))/400)*100

marks2 = [75, 98, 88, 78]
Percentage2 = ((sum(marks2))/400)*100
print(Percentage1, Percentage2)

marks1 = (43, 43, 76, 67)
per = (sum(marks1)/400)*100
print(per)
'''
#Now we can solve this by function and return formula:
'''
def percent(marks):
    Percent = ((marks[0] + (marks[1]) + (marks[2]) + (marks[3]))/400)*100
    return Percent
marks1 = [45, 78, 86,77]
Percentage1 = percent(marks1)

marks2 = [75, 98, 88, 78]
Percentage2 = percent(marks2)
print(Percentage1, Percentage2)

def per(mar):
    per = (((mar[0] + mar[1] + mar[2] + mar[3]))/400)*100
    return per

#mar = (23, 43, 23, 43)
a = int(input("Enter Number 1: "))
b = int(input("Enter Number 1: "))
c = int(input("Enter Number 1: "))
d = int(input("Enter Number 1: "))
mar = (a, b, c, d)
perc = per(mar)
print(perc)
'''

#Quiz:
'''
def greet(name):
    print("Good Day, " + name)

def mySum(num1, num2):
    #return num1 + num2 
    print(num1 + num2)

greet("Harry")
s = mySum(6, 32)

print(s)
'''

#check whether the number is prime or not:
num = int(input("Enter the number: "))
prime = True

for i in range(2, num):
    if(num%i) == 0:
        prime = False
        break
if prime:
    print("This Number is Prime")
else:
    print("This number is not prime")
