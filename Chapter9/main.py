#Use open function to read the content of file...!!
#f = open('sample.txt','r')#function (read 'r') is captured automaticallly

f = open('sample.txt')
#data = f.read()
data = f.read(5)#Read only 5 values
print(data)
f.close()

f = open('another.txt')
data = f.read()
print(data)
f.close()

f = open('sample.txt')
#Read first line:
data = f.readline()
print(data)
#Read second line:
data = f.readline()
print(data)
#Read third line:
data = f.readline()
print(data)
f.close()

'''
#Modes of openning of file:
r = open for reading
w = open for writing
a = open for appending
t = open for updating

'rb' will for read in binary mode
'rt' will open for read in text mode'''

#writing file in python:
f = open('another.txt', 'w')
f.write("Please write on another.txt file by creating this file")
#f.write("Please write on another.txt file by creating this file")#How many times we use function whatever writting txt
f.write("We write as we like")#We can write whatever we want
f.close()

#WITH Statement:
with open('another.txt','r') as f:
    a = f.read()
    print(a)

'''with open('another.txt','w') as f:
    a = f.write('me')
    print(a)'''