'''
KEYWORDS & IDENTIFIERS:
Keywords:
These are reserved words and you cannot use them as constant or
variable or any other identifier names like print,input & for.

Identifiers=
A Python identifier is a name used to identify a variable,function,class,module or
other object. An identifier starts with a letter A to Z or  a to z or an underscore(_)
followed by zero or moe letters,underscope and digits(0 to 9).

DATATYPES & VARIABLES?
Datatypes:
*Numbers=1.Integer 12
         2.complex 5j
         3.Float 45.7
*Sequences Type=1.Strings "mahesh"
                2.List [ ]
                3.Tuple ( )
*Dictionary { }
*Boolen True/False
*Set { }

'''

#Numbers:
a= 23
b= 43.4
c = 4j

print (type(a))
print (type(b))
print (type(c))

print("Done")

#Sequence=
a = "India";
b = [12, 1, 34] #[]=list,()=Tuple, {}=Set
c = ("mumbai","delhi","chennai")

print (type(a))
print (type(b))
print (type(c))

#Boolen=
X = True
print(X)
print(type(X))

#Set=
c ={"India","Africa","Japan","China"}
print(c)
print(type(c))

#Dictionary:
dict = {'Brand':'Lamborghini','Model':'Aventadoor','Colour':'Red'}
print("dict:", dict)
print("car Brand is ",dict['Brand'])
a = input('What would you like to check?')
print("answer is:",dict)

#VARIABLES:
'''it is a name that is used refer to memory location,Python variable is also
known as an identifier and used to hold value.
*Rules for making variable in Python
1.Do not use space while making variables(myname = "mahesh')(my_name = "mahesh")
2.Do not use special symbols while making variables(not use=@ # $ %)
3.Do not use number as first letter of your variable(8list = "list")
'''

name = "Mahesh"
myName2 = "Babu"
my_name = "Mahesh Sutar"

print(name)
print(myName2)
print(my_name)