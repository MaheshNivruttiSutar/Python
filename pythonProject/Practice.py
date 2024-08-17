'''age = int(input("Enter your age:"))
if age>1 and age<18 :
    print("You are under age")
if age>18 and age<45:
    print("You are younger")
if age>46 and age<75:
    print("You are in criteria")
if age>76 and age<99:
    print("You are not eligible")
else:
    print("You are Not fit in criteria")
'''

i = 1
while i<=5:
    print(i)
    i = i + 2
print("Done")

for i in range(10):
    i = i + 1
    print(i)


num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number two:"))
sum = num1 + num2
print("Sum of number is:", sum)

minus = num1 - num2
print("Minis of numbers:", minus)


multiple = num1 * num2
print("Multiple of number is:", multiple)

substraction = num1 / num2
print("Substraction of number is :",substraction)

if num1 > num2:
    print("num1 is greatter than num2")
else:
    print("num2 is greatter than num1")

if num1 == num2:
    print("bothh number are equal")
