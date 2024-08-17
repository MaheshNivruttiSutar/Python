#If you given 4 number and want to find greater number
'''
num1 = int(input("Enter number 1:\n"))
num2 = int(input("Enter number 2:\n"))
num3 = int(input("Enter number 3:\n"))
num4 = int(input("Enter number 4:\n"))

if(num1>num4):
    f1 = num1
else:
    f1 = num4
#print("f1 is equal to:", f1)

if(num2>num3):
    f2 = num2
else:
    f2 = num3
#print("f2 is equal to:", f2)

if(f1>f2):
    print(str(f1) + " is greatest")

else:
    print(str(f2) + " is greatest")
'''
'''
sub1 = int(input("Enter first subjet marks:\n"))
sub2 = int(input("Enter second subjet marks:\n"))
sub3 = int(input("Enter third subjet marks:\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail due to less marks")

elif((sub1+sub2+sub3)/3)<40:
    print("you are fail due to less percentage")
else:
   print("Congratulation !!! You are passed the exam")
'''


text = input("Enter the text:")
if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")