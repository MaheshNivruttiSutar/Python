#Operator:Operators are special symbols in Python that carry out arithmetic or logical computation.
#Operator Overloading:is the ability of a single operator more than one operation
#based on the class(type) of operands.
'''
class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Lets Multiple")
        return self.num * num2.num

n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)
'''

#Other Dendor Method:

class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Lets Multiple")
        return self.num * num2.num

    def __str__(self):
        return f"Decimal Number: {self.num}"

    def __len__(self):
        return

n = Number(9)

print(n)
print(len(n))