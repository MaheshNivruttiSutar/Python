#Prime Number programme:
'''
num = int(input("Enter yor Number: "))
#Prime number are always greater than 1
if num > 1:
    #check for factors
    for i in range(2,num):
        if(num%i)==0:
            print(num,"is not a prime number")
            print(i,"times",num//1,"is",num)
            break
        else:
            print(num,"is a prime number")
else:
    print(num,"is not a prime number")


num = int(input("Enter your Number: "))
prime = True

for i in range(2, num):
    if(num%i)==0:
        print(num, " is not prime")
        break
    else:
        print(num, " is Prime")
        break
'''
#Even and odd number programme:
'''
digit = int(input("Enter your Number: "))
if(digit % 2) == 0:
    print("Number is Even")
else:
    print("Number is odd")

#Convert odd_Even programme into prime number programme:
digit = int(input("Enter your Number: "))
for i in range(2, digit):
        if(digit % i) == 0:
            print("Number is not Prime")
            break
        else:
            print("Number is Prime")
            break
'''
#Convert km to meter:
'''
def meter(km):
    return (km*1000)
k = 1
m = k*1000

print("Conversion in meter is: ",m)'''
#Triangle programme:
'''
n = 4
for i in range(4):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))
print("Programme Done 1")

n = 4
for i in range(4):
    print(" " * (n - i - 1), end="")
    print("*" * (i + 1), end="")
    print(" " * (n - i - 1))
print("Programme Done 2")
n = 4
for i in range(4):
    print("*" * (i+1))
print("Programme Done 3")
n = 4
for i in range(4):
    print(" " * (n - i -1),end="")
    print("*" * (i + 1))'''
#Python Programme to find area of Triangle:
'''a = float(input("Enter first Side:"))
b = float(input("Enter second Side:"))
c = float(input("Enter third Side:"))
#Calculate the semi perimeter:
S= ((a+b+c) / 2)
#Calculate the Area:
Area = (S*(S-a)*(S-b)*(S-c)) ** 0.5
print("Area of Triangle is:",Area)'''
#How to convert list into the set:
'''list = ['Monday','Tuesday','Thursday','Friday','Saturday','Sunday']
print(type(list))
setlist = set(list)
print(setlist)
print(type(setlist))'''
#How to convert a list into a tuple:
'''list = ['Monday','Tuesday','Thursday','Friday','Saturday','Sunday']
print(type(list))
listtuple = tuple(list)
print(listtuple)
print(type(listtuple))'''
#How to convert a list into String:
'''list = ['Monday','Tuesday','Thursday','Friday','Saturday','Sunday']
print(type(list))
listString = ' '.join(list)
print(listString)
print(type(listString))'''
#How to create Empty Numpy Array in python:
'''import numpy
numpy.empty(shape=(0,0))'''

#What is output of below programme:
'''import array
a = [1, 2, 3]
print (a[-3])
print (a[-2])
print (a[-1])'''
#Advance Python Question:
'''names = ['Chris','Jack','John','Daman']
print(names[-1][-1])
print(names[-1][-5])
print(names[-4][-5])'''
#Enumerate function: Adds a counter to an iterable object.This function can accept sequential
#indexes starting from zero
'''subjects = ('Python','Interview','Questions','Result','Joining')
for i,subject in enumerate(subjects):
    print(i, subject)'''
#Create a set with string:
'''objects = {"python","coding","tips","for","beginners"}
#Print set:
print(objects)
print(type(objects))
print(len(objects))

#Use of 'in' keyword:
if "tips" in objects:
    print("These are the best Python coding tips.")

#Use of 'not in' keyword:
if "java tips" not in objects:
    print("These are the best Python coding tips not java tips.")

#Let's initialize an empty set:
items = set()
#Add three string in set
items.add("Python")
items.add("coding")
items.add("tips")
print(items)'''
#Python concatenating string:
'''print('Python'+' is'+' Best'+' Coding'+' language.')
set1 = "I am good boy"
set2 = " and i am from kolhapur"
print(set1 + set2)'''
#How to generate random number in python:
'''
import random
print(random.randrange(1,20,2))
'''
#How to print sum of the numbers starting from 1 to 100?
'''print (sum(range(1, 101)))
print (sum(range(1, 3)))
#How to print sum of odd numbers starting from 1 to 100?
for i in range(1, 10, 2):
     print(i)
print(sum(range(1, 101, 2)))
#How to print sum of Even numbers starting from 1 to 100?
print(sum(range(2, 101, 2)))'''
#What is the output of the programme:
'''names1 = ['Amir','Bear','Charlton','Daman']
names2 = names1
names3 = names1[:]

names2[0] = 'Alice'
names3[1] = 'Bob'

sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10

print(sum)'''
#How to double the list:
'''list1 = [1, 3, 2]
print(list1*2)
print(list("hallo"))'''
#Calculate Average of Number:
'''n = int(input("Enter your Number: "))
a = [ ]
for i in range(0, n):
    elem = int(input("Enter Element: "))
    a.append(elem)
    avg = sum(a)/n
print("Average of elements in the list",round(avg,2))'''

'''n = int(input("Enter your Number: "))
ele = int(input("Enter your Element: "))
Average = n/ele
print(f"Average of Number is {Average}")'''
#Program to reverse the number:
'''n = int(input("Enter Number: "))
rev = 0
while(n>0):
    dig=n%10  #2%2= 0 (Remainder)
    rev=rev*10+dig
    n=n//10   #2//2= 1(Division)
print("The reverse of the number:",rev)'''

#Find Sum of the Digits of Number:
'''n = int(input("Enter a Number: "))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
    print("The Total sum of digit is:",tot)'''
#Python Program to Check if a Number is a Palindrome or Not: Palindrome is number that remains
#same when it's digit are reversed
'''n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a Palindrome Number!")
else:
    print("The number isn't a Palindrome Number!")'''
#Program to Count the Number of Digits in a Number:
'''n=int(input("Enter number:"))
count=0
while(n>0):
    count=count+1
     n=n//10
print("The number of digits in the number is:",count)

num = (input("Enter your number: "))
print(len(num))'''
#Program to Print Table of a Given Number:
'''n=int(input("Enter the number to print the tables for:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)'''
#Python Program to Check if a Number is a Prime Number:
'''num=int(input("Enter number: "))
prime = True
for i in range(2,num):
    if(num%i==0):
        print("Number is not prime")
        break
else:
    print("Number is prime")'''
#Python programme to swap two variable:
'''a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
temp = a
a=b
b = temp
print("The value of 'a' after swapping is",a)
print("The value of 'b' after swapping is",b)'''

#Write continue star:
'''i = 0
for i in range(7):
    print('*')
    i = i+1'''

#Star Programme:
'''n = 4
for i in range(n):
    print(" " * (n-i-1),end="")
    print("*" * (2*i+1),end="")
    print(" " * (n-i-1))'''

'''n = 4
for i in range(n):
    #print("*")
    #print("*" * (n*i))
    print("*" * (n-1*i),end="")
    print(" " * (n-1*i))'''

'''
def km(meter):
    return (meter/1000)
 
m = 2000
k = m/1000

print("Conversion in km is: ",k)'''
