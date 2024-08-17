#A string in python is a sequence of characters...Many Python methods, such as replace, join,
#or split modify strings.
class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9])
print(v1)
print(v2)



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

    def __len__(self):
        return len(self.vec)


v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9])
print(len(v1))
#print(len(v2))
#print(v1*v2)