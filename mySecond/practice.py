'''
mydict = {
    "pankha": "fan",
    "dabba": "box",
    "vastu": "item",
    "ghar": "home"

}
#print("Options are", mydict.keys())#shows word which are in dictinary
#a = input("Enter the hindi word:")
#print("The meaning of your word is:",mydict[a])

#Below line will not throw an error if the word is not present in dictionary
#print("The meaning of your word is:", mydict.get(a))
'''
#write a program to input 8 number from user and display all unique number
num1 = int(input("Enter number 1\n"))
num2 = int(input("Enter number 2\n"))
num3 = int(input("Enter number 3\n"))
num4 = int(input("Enter number 4\n"))
num5 = int(input("Enter number 5\n"))
num6 = int(input("Enter number 6\n"))
num7 = int(input("Enter number 7\n"))
num8 = int(input("Enter number 8\n"))

s = (num1, num2, num3, num4, num5, num6, num7, num8)
print(set(s))#in set unique number are shows

#can we have set with 3 int and 3 str
s = {18, "18", 12, "34", "56"}
print(s)

#s = {20, 20.0, "20"} #in set 20=20.0 so len shows 2
#print(s)
#print(len(s))

s = { }
print(type(s))

#Practice question = 5 (if two names is same then last values give by compiler)
favlang = {}
a = input('Enter your favourite language shubham\n')
b = input('Enter your favourite language ankit\n')
c = input('Enter your favourite language vijay\n')
d = input('Enter your favourite language shubham\n')
favlang['shubham'] = a
favlang['ankit'] = b
favlang['vijay'] = c
favlang['shubham'] = d

print(favlang)
