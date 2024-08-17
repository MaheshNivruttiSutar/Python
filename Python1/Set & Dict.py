#Set in Python{}
'''
set1 = {4,5,1,2,3,6,7}
set2 = {100,95,83,75,63}
print(set1)
print(type(set1))
#set1.add(56)
set1.update(set2)
print(set1)
#set1.remove(1)
#set1.clear()
print(set1)
'''
'''
#Set Union:
set1 = {90,80,70}
set2 = {900,800,700}
set3 = set1.union(set2)
print(set3)
#Intersection in set:We can find common term in set
set1 = {900,80,70}
set2 = {900,800,700}
set3 = set1.intersection(set2)
print(set3)
'''

#Dictionary (Dict) in Python:
thisdict = {
    "Brand": "Chevrolet",
    "Model": "Canaro",
    "Year": 2016,
    "Horsepower": "650BHP"
}

print(thisdict)
print(type(thisdict))
print(thisdict["Brand"])
x = thisdict.get("Model")
print(x)
thisdict["Year"] = 2020 #Replace any value
#thisdict.pop("Year")#Remove value from dict
print(thisdict)
mydict = dict(thisdict)
print("My Dict is:", mydict)
