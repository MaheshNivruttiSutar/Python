#Import programme from another files(main programme):
'''
import main
main.greet("Mahesh")'''

#Global Keyword:IS used to modify the variable outside of the current scope
'''
a = 54 #Global Variable
def func1():
    a = 8 #Local Variable:
    print(a)
func1()
print(a)
'''
'''
a = 54 #Global Variable
def func1():
    global a
    print(f"Print statement 1: {a}")
    a = 8 #Local Variable:
    print(f"Print statement 2: {a}")

func1()
print(f"Print statement 3: {a}")


#Enumerate function:
num1 = int(input("Enter your Number: "))

if (num1 % 2 == 0):
    print("Given number is Even")
else:
    print("Number is odd")
'''
#Use enumerate function to give index number to list item:
'''
list1 =[3, 53, 2, False, 6.2, "Harry"]
index = 0
for item in list1:
    print(index, item)
    index +=1
print(type(list1))
#Short Programme of above programme is:
for index, item in enumerate(list1):
    print(index, item)'''

#List comprehension:
#Use below list and make another list which have Even number from given list
'''
a = [3, 6, 7, 8, 9, 2, 4, 23, 75, 23, 123, 67]
b =[]
for item in a:
    if item%2==0:
        b.append(item)
print(b)

#Shortcut to write the same:
b = [i for i in a if i%2==0]
print(b)
'''
#Using a list make another set:
t = [1, 4, 2, 4, 1, 2, 3]
s = {i for i in t}
print(s)
