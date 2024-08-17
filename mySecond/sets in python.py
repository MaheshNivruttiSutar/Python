b = { 1, 2, 3, 4, 1} #Symbol of Set { }
# Important : This syntax will create an empty dictionary and not an empty set
print(type(b))
d = [ ]
print(type(d))
c = ( )
print(type(c))
a = {}
print(type(a))
print(a)

# An empty set can created by using the below syntax
b = set()
print(type(b))
# if yo want to add value in set then
b.add(4)#If we added same value both time then it's consider only one time value
b.add(4)
b.add(6)
b.add(7)
b.add(8)
b.add(6)#Adding a value repeatedly can't change a set
print(set(b))
print(len(b))#Print the length of the set
b.remove(7) # Remove 7 from given set b
#b.remove(15) #throws as error while value is not available in set
print(b)
#print(b.pop()) #Remove an (first) arbitary value from set
print(b)
