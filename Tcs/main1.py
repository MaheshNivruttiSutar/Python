#Python Program to Check if a Number is an Armstrong Number:is a number that is equal
#to the sum of cubes of it's digit 371=3**3+7**3+1**3
'''n=int(input("Enter any number: "))
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
if(sum(b)==n):
    print("The number is an armstrong number. ")
else:
    print("The number isn't an arsmtrong number. ")'''

#Python Program to Check if a Number is a Perfect Number:is a positive integer
#that is equal to sum of its positive divisors,excluding the number itself.
#6 has divisors 1 2 3 and 1+2+3=6
'''n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
        if (sum1 == n):
            print("The number is a Perfect number!")
    else:
        print("The number is not a Perfect number!")'''

#Python Program to Check if a Number is a Strong Number:a special number whosesum of factorial
#of digit is equal to original number 2!=2 145!=145
'''sum1=0
num=int(input("Enter a number:"))
temp=num
while(num):
    i=1
    f=1
    r=num%10
    while(i<=r):
        f=f*i
        i=i+1
        sum1=sum1+f
        num=num//10
        if(sum1==temp):
            print("The number is a strong number")
        else: 
            print("The number is not a strong number")'''

#Python Program to Find the Second Largest Number in a List:
'''a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
    a.sort()
    print("Second largest element is:",a[n-2])'''

#Python Program to Swap the First and Last Value of a List:
'''a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
a.append(element)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print("New list is:")
print(a)'''

#Python Program to Check if a String is a Palindrome or Not:
string= input("Enter string:")
if(string==string[::-1]):
    print("The string is a palindrome")
else:
    print("The string isn't a palindrome")

#Python Program to Count the Number of Vowels in a String:
string=input("Enter string:")
vowels=0
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels=vowels+1
        print("Number of vowels are:")
print(vowels)

#Python Program to Check Common Letters in Two Input Strings:
s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)&set(s2))
print("The common letters are:")
for i in a:
    print(i)

'''def ReverseCharBridge(n):
    for i in range(n):
        for j in range(ord('A'), ord('A') +
                                 (2 * n) - 1):
            if j >= (ord('A') + n - 1) + i:
                print(chr((ord('A') + n - 1) -
                          (j % (ord('A') + n - 1))), end='')

            elif j <= (ord('A') + n - 1) - i:
                print(chr(j), end='')
            else:
                print(end="")
        print("\n", end='')


# Driver Code
n = 7
ReverseCharBridge(n)


n=0
for i in range(71,64,-1):
    for j in range(65,i+1):
        a=chr(i)
        print(a, end=" ")
    if n>0:
        for l in range(1,3+(n-1)*4):  
            print(end="")
    if i<71:
        j=j+1
    for k in range(j-1,64,-1):
        b=chr(k)
        print(b, end=" ")
    n=n+1
    print()'''