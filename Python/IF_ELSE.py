#IF_ELSE  STATEMENT:
age = int(input("Enter your age:"))
if age > 1 and age < 18:
    print("You are not eligible for registration")
elif age >= 18 and age <= 90:
    print("You are eligible for registration")
    if age > 25 and age < 50:
        print("You are to Young! (nested if)")
    else:
        print("You are in mid-range")
else:
    print("Our recommandation is to make Oldage Cards")
'''
#Switch Case Statement:Decision making switch
def day1():
    return "Monday"
def day2():
    return "Tuesday"
def day3():
    return "Wednsday"
def day4():
    return "Thursday"
def day5():
    return "Friday"
def day6():
    return "Saturday"
def day7():
    return "Sunday"
def default():
    return "Incorrect Day"

switcher = {
    1: day1,
    2: day2,
    3: day3,
    4: day4,
    5: day5,
    6: day6,
    7: day7

}
def switch(dayweek):
    return switcher.get(dayweek, default)()

input = int(input("Please Enter Day number 1 to 7 ?"))
print(switch(input))'''

#Loop in Python:(While, For, Nested)
#1.For Loop: Need Parameter and Indexes
#2.While Loop:Run whenever not get false value
'''
#While Loop:
i = 1
while i < 11:
    print(i)
    i = i+1


#For Loop:
num = int(input("Enter a number for table: "))

for a in range(1, 11):
    #print(num, 'x', a, '=', num*a)
    print(f"{num}X{a}={num*a}")
'''
'''
#Nested Loop:
colour = ["Red", "Yellow", "Black"]
car = ["Nano", "Zen", "Swift"]

for x in colour:
    for y in car:
        print(x, y)
'''