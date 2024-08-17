#Dictionary and Sets
mydict = dict(
    fast="In quick manner",
    marks=[2, 3, 4, 5],
    day="monday",
    colour="red",
    success="patience",
    love="hate")

print(mydict["day"])
print(mydict["marks"])
#print(mydict["success"])
#print(mydict["colour"])
#print(mydict["love"])
print(mydict.keys()) #print the keys of dictionary
#print(list(mydict.keys()))
#mydict["marks"] = [4, 32, 33, 43]#previous value replaced in dict
#print(mydict["marks"])
print(mydict.values()) #print the key of dictionary
#print(mydict.items()) #print all keys of dictionary
'''updatedict = {
    "lovish": "friend",
    "sun": "hot",
    "day": "sunday" #update previous data
}
mydict.update(updatedict) #update the dictionary by adding key values
print(mydict)'''

#print(mydict.get("marks"))#print value associated with marks
#print(mydict["marks"])#print value associated with marks

#The difference between .get and [] sytax in dictionary
print(mydict.get("marks2"))#returns none as marks2 is not present in dictionary
#print(mydict["marks2"]) #throws as error as marks2 is not present in dictionary


s = { }
print(type(s))
