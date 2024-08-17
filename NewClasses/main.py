#While Loop:
count = 0

while count<9:
    print("Number:", count)
    count = count+1

print("Good Bye")



import random
n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:#not equal to  !=
    guess = int(input("New number:"))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number too small")
        else:
            print("sorry that you are giving up!")
    else:
        print("Cogratulation, You made it!")

#For loop:for loop is a python loop which repeat group of statement a specific number of item
fruits = ['Mango', 'Grapes', 'Watermelon', 'Banana', 'Orange', 'apple']
for fruit in fruits:
    print("current fruits:", fruit)
print("Good bye")

#Factorial= 3!, 6!
num = int(input("Number:"))
factorial = 1

if num < 0:
    print("must be possitive")
elif num == 0:
    print("factorial = 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
print(factorial)