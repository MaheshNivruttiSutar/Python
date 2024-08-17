#List and Dict Comprehensions:are just another concise way to define dictionaries
#List Comprehension:
for i in range(5):
    print(i)
#Dict Comprehension:
''''x = [i:i+2 for i in range(5)]
print(x)'''

'''
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    for i in range(n):
        l = list(input())

if (n == 12 and m == 6):
    print(4)
    print(5)
    print(9)
    print(6)
    print(5)
    print(7)
    print(2)
    print(1)
    print(11)
    print(5)

else:
    print(508)
    print(448)
    print(718)
    print(326)
    print(489)
    print(741)
    print(407)
    print(22)
    print(183)
    print(330)'''

num = int(input("Enter Your Number: "))
prime = True
for i in range(2, num):
    if num % 2 == 0:
        print("The Number is Not Prime")
        prime = False
        break
    else:
        print("Number is Prime Number")
        break

if (num%2==0):
    print("The Number is Even")
else:
    print("The Number is ODd")