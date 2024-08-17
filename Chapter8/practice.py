#Maximum Program:
'''
def maximum(num1, num2, num3):
    if(num1>num2):
        if(num1>num3):
            return num1
    else:
        if(num2>num3):
            return num2
        else:
            return num3

m = maximum(13, 44, 43)
#print("The value of the maximum is: " + str(m))
#print(f"The value of the maximum is: {m} ")
print("The Value Of Maximum is: ",m)
'''

'''
def max(a, b, c):
    if (a<b):
        if(a<c):
            return a
    else:
        if b<c:
            return b
        else:
            return c
m = max(12, 343, 32)
print("Max Number is: ", m)
'''
#Minimum Program:
'''
def minimum(num1, num2, num3):
    if(num1<num2):
        if(num1<num3):
            return num1
    else:
        if(num2<num3):
            return num2
        else:
            return num3

m = minimum(13, 44, 43)
print("The value of the minium is: " + str(m))
'''
#Convert Celcius to Ferhanate:
'''
def farh(cel):
    return (cel *(9/5)) + 32

c = 0
f = farh(c)
print("Farheit Temperature is " +str(f))
'''
#Print more function without space:
'''
print("Hi")
print("I am")
print("Mahesh")

print("Hi,", end="")
print("I am", end=" ")
print("Mahesh", end=" ")

print("Done")

print("Hi,", end="")
print("I am", end=" ")
print("Mahesh", end="")
'''
'''
def metre(km):
    return(km*1000)

k = 1
m = metre(k)
print("metre is: " + str(m))
'''
'''
#Convert inches to centimeter:
def cent(inch):
    return (inch * 2.54)
# 1inch = 2.54Centimetre
inch = 1
c = cent(inch)
print("Centimetre is: " +str(c))
'''

#Star Program:
'''
n = 5
for i in range(n):
    print("*" * (n-i))
'''

#Using Strip Function:
'''
this = "     Mahesh is good boy   "
print(this)
print(this.strip())
'''


def remove_and_split(string, word):
    newStr = string.replace(word, " ")
    return newStr.strip()

this ="   Mahesh is good boy   "
n = remove_and_split(this, "Mahesh")
print(n)

'''
def metre(km):
    return(km*1000)

k = int(input("Enter value for k: "))
m = metre(k)
print("metre is: " + str(m))
'''

