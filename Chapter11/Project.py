'''
import random
randNumber = random.randint(1, 5)
print(randNumber)

#Guessing Game:
import random
randNumber = random.randint(1, 5)
print(randNumber)

userGuess = int(input("Enter your guess: "))
if(userGuess==randNumber):
    print("You guessed it right!!")
else:
    print("You guessed it wrong!!")

#By Taking multiple input find right number :
import random
randNumber = random.randint(1, 5)
print(randNumber)
userGuess = None
guessses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    if(userGuess==randNumber):
        print("You guessed it right!!")
    else:
        print("You guessed it wrong!!")
'''
#Modification:
import random
randNumber = random.randint(1, 100)
#print(randNumber)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("You guessed it right!!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong!! Enter a smaller number")
        else:
            print("You guessed it wrong!! Enter a larger Number")

print(f"You guessed the number in {guesses} guesses")
''