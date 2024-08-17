'''
a = input("Enter first Number:")
b = input("Enter second Number:")
a = int(a)
b = int(b)
#Avarage
avg = (a + b) / 2
print("Average is:", avg)
'''

#Create a list using []
a = [1, 2, 4, 56, 6]
#Print a list using print function:
print(a)
#Access index using a[0], a[1], a[2]
print(a[2])
print(a[4])

#Change the value of list using:
a[0] = 98
print(a)


#We Can Create a List With Items Of Different Type:
c = [45, "Harry", False, 6.9, True]
print(c)
print(type(c))


#slice operation

story ="My name is Mahesh,From kolhapur. i have completed My graduation in BE-MECHANICAL. Currently i am searching a job"
print(story)
print(story[0:6])
print(story[1:7:1])
print(story[1:7:3])   #(Starting Point:End Point:Gap)
print(story[-7])
print(len(story))


f = input("Enter your N umber: ")
print(f)