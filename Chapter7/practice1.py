#star print in various sequences:
'''n = 4
for i in range(4):
    print("m" * (i+1))

n = 7
for i in range(7):
    print(" " * (n-i-1),end="")
    print("*" * (2*i+1),end="")
    print(" " * (n-i-1))'''

'''
n = 4
for i in range(4):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))
'''
'''
#Print multiplication factor in reverse order
num = int(input("Enter the number:"))
for i in range(1, 11):
    #print(str(num) + " X " + str(i) + "=" + str(i*num))
   #print(f"{num}X{i}={num*i}") #By using f string
    print(str(num) + " * " + str(i) + "=" + str(num*i))
'''
#Factorial:
# n!= 1 x 2 x 3 X 4 X 5 X........X n
# 5! = 1 X 2 X 3 X 4 X 5

n = 4
for i in range(4):
    print("m" * (n-i))


n = 3
for i in range(n):
    print(" " * (n-i), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i))
