#Lambda Function:An Anonymous(Ninavi) function is known as lambda function.
#This function can have a number of parameter but,just can have one statement
'''
a = lambda x,y:x+y
print(a(5,6 ))

a = lambda x,y,z:x+y+z
print(a(5,6,7))
print("End of Lambda Function")

#What does [::-1] do?
import array as arr
a = arr.array('i',[1,2,3,4,5,6])
print(a)
num=a[::-1] #Inverse the string
print(num)
print("Inverse Array programme")'''

#How can you randomize the items in list:
'''
from random import shuffle
x = ['keep','Blue','Flag','Flying','High']
print(x)
shuffle(x)
print(x)
print("shuffle function used to randomize the items in the list")'''

#How we can generate random number in python: 1)Import random 2)random.random

import random
print("Random value between 0 to 9 is:",random.randint(0,9))

#Random generators:There are four type of random generator's
#1)randrange(a, b):It returns the element by selecting it randomly from range:(Start,Stop,Step)
import random
print(random.randrange(1,20,2))
#2)uniform(a,b):It chooses floating point number that is defined in the range:
import random
print(random.uniform(1,8))
#3)normalvariate(mean, sdev):It is used for the normal distribution where the nu is mean and
#sdev is a sigma that is used to standard deviation.
import random
print(random.normalvariate(1,2))

#4)The random class:It is used and instantiated creates independent multiple random number generators.
#import random
#print(random.class(23))