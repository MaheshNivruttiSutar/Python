#Play game and score hiscore in txt file
'''
import random
randNumber = random.randint(1, 100)
print(randNumber)
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

with open("hiscore.txt", "w") as f:
    f.write(str(guesses))
'''

#After complition of game hiscore will be store in "hiscore.txt" file

import random
randNumber = random.randint(1, 100)
print(randNumber)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    try:
        userGuess = int(input("Enter your guess: "))
        guesses += 1
        if(userGuess==randNumber):
            print("You guessed it right!!")
        else:
            if(userGuess>randNumber):
                print("You guessed it wrong!! Enter a smaller number")
            else:
                print("You guessed it wrong!! Enter a larger Number")
    except Exception as e:
        print(f"Error occur due to {e}")

print(f"You guessed the number in {guesses} guesses")

with open("hiscore.txt", "w") as f:
    f.write(str(guesses))

