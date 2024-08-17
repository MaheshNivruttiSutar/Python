#write a program which shows name present in list or not
names = ["harry", "ram", "yogesh", "shilpa", "sunil", "vijay", "sourabh"]
print(names)
name = input("Enter the name to check:\n")

if name in names:
    print("Your name is present in list")
else:
    print("Your name is not present in list")
'''


marks = int(input("Enter your marks:\n"))

if marks>90:
    grade = "EXCELLENT"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks>=50:
    grade = "D"
elif marks>=40:
    grade = "E"
else:
    grade = "Fail"

print("Your grade is:", grade)
'''