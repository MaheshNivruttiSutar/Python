#Recursion is a function which call itself. It is directly used in mathematic formula :
'''
#n! = 1 * 2 * 3 * 4.....* n
n = int(input("Enter one number: "))
#n = 1
product = 1
for i in range(n):
    product = product * (i+1)
print(product)
'''

#Another method:
'''
def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

print(factorial_iter(5))
'''

#Recursion:
'''
#n! = 1 * 2 * 3 * 4.....* n
#n! = 1 * 2 * 3 * 4....* (n-1) * n
#n! =  n * (n-1)!
def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product
f = factorial_iter(3)
print(f)


def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)
'''

'''
def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)

f = factorial_iter(3)
print(f)
'''

#Use Recursion function to calculate sum of first n natural number
#sum =
def recur_sum(n):
    if n <= 1:
        return n
    else:
        return n + recur_sum(n-1)

#Give Number from user
num = int(input("Enter your Number: "))
if num < 0:
    print("Enter Positive number")
else:
    print("The Sum is",recur_sum(num))