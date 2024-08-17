#Array in python created after importing the array module.
#THree methods to create Array:
#1] Import Array
#2] Using Alians
#3] Using *
'''
#Import Array:
import array
a=array.array('i',[1,2,3,4,5,6])
print(a)
#Using Alians:
import array as arr
a=arr.array('i',[1,2,3,4,5,6])
print(a)
#Using *  :
from array import *
a=array('i',[1,2,3,4,5,6])
print(a)
#Accessing Element:
num = a[2]
num1 = a[-4]
print(num)
print(num1)

#Basic Array Operations:
#Finding length of an Array:
length = len(a)
print(length)
print(len(a))
'''

#Adding Element to the Array:There are three main method to add array
'''
# 1]Append 2]Extend 3]Insert
#(1)append=Used when you want to add a single element at the end of the array:
import array
a = array.array('d',[2.1,2.3,4.3])
print(a)
a.append(6.7)
print(a)
print("Append Operation Done....!")

#(2)Extend=Used when you want to add more than one element at the end of an array:
#Note:In extend condition you want to use square bracket compalsory:
import array as arr
b = arr.array('i',[11,12,13,14,15,16])
print(b)
b.extend([23,32,54])
print(b)

import array
c = array.array('i',[2, 4, 6, 8])
print(c)
c.extend([10, 12, 14, 16, 18])
print(c)

from array import *
d = array('i',[11, 12, 13, 14, 16])
print(d)
d.extend([18, 20, 22, 24])
print(f"d array = {d}")
print("Extend Operation Done...!")

#(3)Insert:Used when you want to add an element at a specific position in an array:
#Command does not remove already given value at that place:
from array import *
c = array('i',[12,24,60,72])
print(c)
c.insert(2, 36)
print(c)
c.insert(3,48)
print(c)
print("Insert Operation Done....!")
'''
#Removing elements of an array:
#There are two Methods: 1)POP 2)REMOVE
'''
#POP:Used when you want to remove an element and return it.
import array
a = array.array('i',[1,2,3,4,5,6,7])
print(a)
a.pop()  #Last Value
print("Last Value Remove",a)
a.pop(2) #Index 2 Value can be Remove
print(a)
a.pop(-2) #Index -2 value can be deleted
print(a)
print("End Of POP")

#REMOVE:Used when you want to remove an element with a specific value without returning it.
import array as arr
b = arr.array('i',[11,12,13,14])
print(b)
b.remove(11)
print(b)'''

#Array Operation 1]Concatenation 2]Slicing
'''
#Array Concatenation:Can be done using "+" symbol
import array
a = array.array('i',[11,12,13])
b = array.array('i',[14,15,16])
#c = array.array('i')
c = a+b
print("Array C is:", c)

#Slicing an Array: Slicing using the symbol ":" ,This returns a range of elements that
#we have specified by the index Number.
import array
d= array.array('i', [11, 12, 13, 14, 15, 16])
print(d[0:2])

import array
a = array.array('i',[1, 2, 3, 4, 5, 6, 7, 8])
print(a)
print(a[1:6])'''

#Looping through an Array:Using for and while loop
'''
#For:Iterates over the items of an array specified number of times.
import array as arr
a = arr.array('d',[1.1,2.2,3.3,3.1,3.7])
print(a)
for i in a:
    print(i)
print("For Loop Operation Ended...")

#While:Iterates over the elements until a certain condition is met.
import array as arr
a = arr.array('d',[1.1,2.2,3.3,3.1,3.7])
b = 0
while b<len(a):
    print(a[b])
    b=b+1
'''