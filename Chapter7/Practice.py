#Multiplication table of any number
'''
num = int(input("Enter the number:"))
for i in range(1, 11):
    #print(str(num) + " X " + str(i) + "=" + str(i*num))
   print(f"{num}x{i}={num*i}") #By using f string

a = 21
for i in range(1, 11):
    #print(f"{a}X{i}={num*i}")
    print(str(a) + "X" + str(i) + "=" + str(i*a))


#greet name which start with s
l1 = ["harry", "soham", "sachin", "rahul"]

for name in l1:
    if name.startswith("h"):
       print(name)

'''
'''
#To cheack wheather it is prime number or not:
num = int(input("Enter a Number: "))
#Prime number are always greater than 1
if num > 1:
    #check for factors
    for i in range(2,num):
        if(num%i)==0:
            print(num,"is not a prime number")
            print(i,"times",num//1,"is",num)
            break
        else:
            print(num,"is a prime number")
else:
    print(num,"is not a prime number")
'''
'''
num = int(input("Enter your Number: "))
if num > 1:
    for i in range(2,num):
        if(num%i)==0:
            print("Given number is not prime")
            #print(i,"times",num//1,"is",num)
            break
        else:
            print("Given Number is Prime")
            break
else:
    print(num,"is not a prime number")
    '''