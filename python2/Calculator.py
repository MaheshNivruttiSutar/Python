def calculator(num1, sign, num2):
    if sign == "+":
        return num1+num2
    elif sign == "-":
        return num1-num2
    elif sign == "*":
        return num1*num2
    elif sign == "/":
        return num1/num2
    elif sign == "%":
        return num1%num2
    elif sign == "**":
        return num1**num2
    elif sign == "//":
        return num1//num2
    else:
        print("Something Missing..!")

a = int(input("Enter 1st Number : "))
b = input("Enter Operation : ")
c = int(input("Enter 2nd Number : "))

print("Your Answer is: ", calculator(a,b,c))



#my own program:
def combination(sen1, sen2):
    return(sen1 + sen2)

a = input("Enter sen1:")
b = input("Enter sen2: ")

print("my whole sentence is", combination(a,b))