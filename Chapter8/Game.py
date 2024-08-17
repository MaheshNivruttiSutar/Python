#Snake water gun
import random
def gamewin(comp, you):
 if comp == you:
    return None
#Cheak for all possibility when comp choose 's'
 elif comp == 's':
    if you == 'w':
        return False
    elif you == 'g':
        return True

#Cheak for all possibility when comp choose 'w'
 elif comp == 'w':
    if you == 'g' :
       return False
    elif you =='s':
       return True

#Cheak for all possibility when comp choose 'g'
 elif comp == 'g':
    if you == 's':
       return False
    if you == 'w':
        return True

print("Comp turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your turn: Snake(s) Water(w) or Gun(g)?")
a = gamewin(comp,you)

print(f" Computer choose: {comp}")
print(f" You choose: {you}")

if a == None:
    print("The game is tie!")
elif a:
    print("You win!")
else:
    print("You Lose!!")