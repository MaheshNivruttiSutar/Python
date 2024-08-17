#How to find vector:
#Vector:A vector is a one-dimensional array of lists.
'''
class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i} a{index}"
            index += 1
        return str1

v1 = Vector([1, 4, 6, 8])
print(v1)'''


class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i} a{index} +"
            index += 1
        return str1

v1 = Vector([1, 4, 6])
print(v1)

class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i} a{index} +"
            index += 1
        return str1[:-1]

v1 = Vector([1, 4, 6])
print(v1)

class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i} a{index} +"
            index += 1
        return str1[:-1]

v1 = Vector([1, 4, 6, 45, 434])
print(v1)


#Find Sum of two vector:
'''
class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i} a{index} +"
            index += 1
        return str1[:-1]

    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)

    def __mul__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)


v1 = Vector([1, 4])
v2 = Vector([1, 6])
print(v1)
print(v2)
print(v1+v2)'''

#Find Product of two vector:
'''
class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i} a{index} +"
            index += 1
        return str1[:-1]

    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum


v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9])
print(v1)
print(v2)
print(v1*v2)'''
