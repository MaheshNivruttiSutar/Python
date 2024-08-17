#Break and Continue Statement:
#Continue Statement: When we use continue value will get skipped.
for var in "world":
    if var == "l":
        continue
    print(var)

print("Loading.....")

#Break Statement:After Break All program will stop
for var in "World":
    if var == "l":
        break
    print(var)
print("Statement End")

'''
#List[] and Tuple() in Python: Set{}
#List in Python:
carlist = ["Toyota", "Nissan", "Lexus", "Minni"]
print(carlist)
owner = ["Suresh", "Ramesh", "Vijay", "Akash"]
print(type(carlist))
print(carlist[1])
print(len(carlist))
print(len(carlist[2]))
carlist[0] = "Fortuner" #Replace value at given position
#carlist[0] = ["Fortuner","Land Cruiser"] #Adding two input at one place
carlist.append("Lotus") #Add given value at last
print(carlist)
carlist.insert(3, "Hummer")
print(carlist)
carlist.sort() #Arrange in Alphabetical Order
print(carlist)
carlist.remove("Minni")
print(carlist)
carlist.pop(1)#Remove value at specific position
print(carlist)
combine = carlist + owner
print(combine)
'''
''''#Tuple in Python:
cartuple = ("Maruti", "Ford", "Flat", "Tata", "Volkswagon")
print(cartuple)
print(type(cartuple))
#cartuple.append("Volvo")
#print(cartuple)
#Note: In tuple we can't do some operation so we can convert tuple into list
carlistt = list(cartuple)#Convert Tuple into list
print(carlistt)
carlistt.append("Volvo")
print(carlistt)
carlistt.remove("Tata")
print("carlistt")
newtuple = tuple(carlistt)#Again convert into tuple
print(newtuple)'''
'''
var = (1,2,3,4,5,6,7,8,9,3,7,3)
x = var.count(3)
print(x)
'''