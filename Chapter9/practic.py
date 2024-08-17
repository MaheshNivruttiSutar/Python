#from one txt file if you want to replace something:
'''
with open("this.txt", 'r') as f:
    content = f.read()

content = content.replace("donkey", "$%@$^#")

with open("this.txt","w") as f:
    content = f.write(content)



with open("this.txt")as f:
    data = f.read()
data = data.replace("Kolhapur", "Pune")

with open("this.txt", 'w')as f:
    data = f.write(data)
'''
'''
#Replace Large number of words:
words = ["pune", "kolhapur", "nagpur"]

with open("this.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "$%@$^#")
    with open("this.txt","w") as f:
        f.write(content)
'''
'''
#Using programme copy the txt file:
with open("this.txt") as f:
    content = f.read()

with open("copy.txt","w") as f:
    f.write(content)
'''
'''
#Check whether two file are equal or not:
file1 = "copy.txt"
file2 = "sample.txt"

with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print("files are identical")
else:
    print("files are not identical")
'''
'''
#Remove all content from any file:
filename = "copy.txt"
with open(filename, "w") as f:
    f.write("hbbfhgbdfgsdkj ")
'''

#Rename file using python programme:
'''
import os
oldname = "sample.txt"
newname = "renamed_by_python.txt"
with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)

os.remove(oldname)
'''

import os
Oldname = "   "
newname = "sample.txt"

with open(Oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)

os.remove(Oldname)