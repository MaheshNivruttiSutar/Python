#Nested loop:Let's write a code with pythagorean number(a^2 + b^2 = c^2)
from math import sqrt
n = int(input("Maximum Number:"))
for a in range(1,n+1):
    for b in range(a,n):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if ((c_square - c**2) == 0):
            print(a, b, c)

#BULK Reservation of train(Name,Age,Sex)
travelling = input("yes or no:")

while travelling == 'yes':

    num = int(input("Number of people travellings:"))
    for num in range(1, num+1):
        name = input("name:")
        age = input("age:")
        sex = input("male or female:")
        print(name)
        print(age)
        print(sex)
        travelling = input("Oops1! forget someone?")