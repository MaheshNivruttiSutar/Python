'''The operator can be defined as a symbol which is responsible for a
    particular operation between two operands.
    1.Arithmetic Operator { +,-,*,%,/,**,// }
    2.Comparison Operator { ==,!=,<,>,<=,>= }
    3.Assignment Operator { +=,-=,*=,/=,**= }
    4.Logical Operator { and,or,not }
    5.Bitwise Operators { &,|,^,~,<<,>> }
    6.Membership Operators { in,not in }
    7.Identity Operators { is,is not }
'''
'''
#Arithmetic opertor:
x = 7
y = 3

print("The Addition is:", x + y)
print("The Substraction: is:", x - y)
print("The Multiplication is:", x * y)
print("The Divide is:", x / y)
print("The Modulus is:", x % y)
print("The Explonation is:", x ** y)
print("The Floor Division is:", x // y) #Floor division means integer division operator 7//3=2
'''

'''#Assignment Operator
x = 5
x += 3
print(x)
x = 6
x -= 3
print(x)
x =7
x *= 3
print(x)
x = 5
x /= 3
print(x)
x = 2
x **= 3
print(x)'''
'''#Comparison Operator:
x = 5
y = 3

print("Comparison is:", x == y)
print("Comparison is:", x != y)
print("Comparison is:", x < y)
print("Comparison is:", x > y)
print("Comparison is:", x <= y)
print("Comparison is:", x >= y)'''

'''#Logical Operator:
x = 5
y = 3
print(x == 5 and y == 3) #Both statement require true
print(x == 5 and y == 4) #Both statement require true
print(x == 5 or y == 4) #One value most require true
print(not(x == 7 and y == 3)) #One value most be wrong
print(not(x == 5 and y == 3)) #One value most be wrong'''

'''#Bitwise Operator:
x = 7
y = 2

print("Bitwise for XOR:", x ^ y)
print("Bitwise for OR:", x | y)
print("Bitwise for AND:", x & y)
print("Bitwise for NOT:", (~(x)))#Not value is for one variable only
print("Bitwise for LS:", x << 2)#Left Shift: 7*2=14,14*2=28
print("Bitwise for RS:", x >> 2)#Right shift: 7/2=3.5, 3/2=1.5'''

#Membership Operator:
s = ["India","Pakistan"]
print("India" in s)
print("India" not in s)

#Identity Operator:
x = ["Green","Yellow","White","Red","Blue","Black"]
y = ["Green","Yellow","White","Red","Blue","Black"]
z = x
print("m")
print(x is z)
print("a")
print(x is y)#x root value is change
print("b")
print(x == y)#x normal value is equal
print("c")
print(x is not y)#Function using root value
print("d")
print(x != y)#Function using normal value
