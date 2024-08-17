#Expection Handling:Usefull to run programme continuosly without Breaking/Crashing
'''
while(True):
    print("Press q to quit")
    a = input("Enter a number: ")
    if a == 'q':
        break
    try:
            print("Trying...!")
            a = int(a)
            if a>6:
                print("You Entered a Number Greatter than 6")
    except Exception as e:
        print(f"Your Input Resulted in a Error {e}")
print("Thanks for playing this game")
'''
'''
while(True):
    print("Press q to quit")
    a = input("Enter a Number: ")
    if a == 'q':
        break
    try:
        print("Trying....")
        a = int(a)
        if a>6:
            print("You entered a number greatter than 6")

    except Exception as e:
        print(f"Your Input Resulted in a Error {e}")

print("Thanks for playing this Game")
'''

#Handing different Exception:
'''
try:
    a = int(input("Enter a Number: "))
    c = 1/a
    print(c)
except Exception as e:
    print("Exception Occured")
    print(e)
print("Thanks for using this code..!!")
'''
'''
try:
    a = int(input("Enter a Number: "))
    c = 1/a
    print(c)
except ValueError as e:
    print("Exception1 Occured")
    print(e)

except ZeroDivisionError as e:
    print("Exception2 Occured")
    print(e)

print("Thanks for using this code..!!")
'''
'''
try:
    a = int(input("Enter a Number: "))
    c = 1/a
    print(c)
except ValueError as e:
    print("Please Enter a valid Value")
    print(e)

except ZeroDivisionError as e:
    print("Make sure that you are not dividing by 0")
    print(e)

print("Thanks for using this code..!!")'''

#Raising Excpeption:Create our own exception
def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good = Harry")
a = increment(34) #Also put fjgndfj
print(a)

'''
#Try with Else Clause:
try:
    i = int(input("Enter a Number: "))
    c = 1/i
except Exception as e:
    print(e)
else:
    print("We Were Successful...!")


#Try with Finally:
try:
    i = int(input("Enter a Number: "))
    c = 1 / i
except Exception as e:
    print(e)
    exit()
finally:
    print("We Are done...!")
'''
'''
def greet(name):
    print(f"Good Morning,{name}")

n = input("Enter a Name:\n")
greet(n)

'''
#If you want to not run file in other file:
def greet(name):
    print(f"Good Morning,{name}")

if __name__ == "__main__":
    n = input("Enter a Name:\n")
    greet(n)