#Function in Python:
'''
def add(x, y):
    return x+y

print(add(8, 6))

def minus(X, Y):
    return X-Y

print(minus(9, 4))

def multiple(X, Y, Z):
    return X*Y*Z


print(multiple(2, 4, 3))

def fun_nation(country):
    return(" I am From " + country)


print(fun_nation("India"))

def fun_festival(marathi):
    return("My favourite Festival is " + marathi)


print(fun_festival("Holi"))
'''
'''
def fun_admit(name, age, phone, city, country, gender):
  print("Student Name is {0} his/her age is {1} and Phone Number is {2} Lives in {3} Situated in {4} his/her gender is {5}".format(name, age, phone, city, country, gender))

#fun_admit("Mahesh", 18, 9637811336, "Kolhapur", "India","male")
#fun_admit("Umesh", 17, 8390466067, "Kolhapur", "India", "male")
#fun_admit("Vikas", 17, 9011831061, "Pune", "India", "male")
#fun_admit("Vijay", 20, 8007107800, "Mumbai", "India", "male")

a = str(input("Ener Name : "))
b = int(input("Enter Your Age : "))
c = int(input("Enter phone Number :"))
d = str(input("Enter City : "))
e = str(input("Enter Country : "))
f = str(input("Enter your Gender: "))

fun_admit(a,b,c,d,e,f)
'''
#Recursion in Python:
'''
In Python we know that a function can call other functions. It is even possible for the
    function to call itself. These types of construct are termed as recursive functions.
    
Advantages of Recursion:
1.Recursive functions make the code look clean and elegant.
2.A Complex task can be broken down into simpler sub-problemusing recursion.
3.Sequence generation is easier with recursion than using some nested iteration.
'''

def factorial(x):

    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))

inp = int(input("Enter Number for factorial : "))
print("The Factorial of", inp, "is", factorial(inp))