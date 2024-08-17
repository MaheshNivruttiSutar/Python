#Write programme to open 3 files (1.txt, 2.txt, 3.txt),If any of the file is missing then msg should be
#seen without existing programme:
'''
def readFile(filename):
    try:
        with open(filename,'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")

readFile("1.txt")
readFile("2.txt")
readFile("3.txt")
'''
#Create File:
'''
f = open('3.txt', 'w')
f.write("Hi,This is Mahesh")
f.close()'''
#Write a programme to print third,fifth and seventh element from list using enumerate function:
'''
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index, item in enumerate(l):
    if index==4 or index==6 or index==8:
        #print(index-1,item)
        print(f"The {index+1} element is {item}")'''
#Write a programme to print a ist which contain multiplication table of user intered number:
'''
num = int(input("Enter your Number: "))
table = [num*i for i in range(1, 11)]
print(table)
'''
#Write a programme to display a/b where a and b are integers, if b=0,display infinite by handling th ZeroDivisionError
'''
a = int(input("Enter Number a: "))
b = int(input("Enter Number b: "))
try:
    print(a/b)
except Exception as e: 
    print("Infinite")'''

#Create a multiplication table and store in file Tables.txt:
num = int(input("Enter your Number: "))
table = [num*i for i in range(1,11)]
print(table)
with open("Tables.txt",'a') as f:
    f.write(str(table))
    f.write('\n')
