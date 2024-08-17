#Create poem.txt and find word is present in file or not
f = open('poem.txt')
data = f.read()
if 'twinkle' in data:
    print("Twinkle is present")
else:
    print("Twinkle is not Present")
f.close()


'''
#Create program which change game score
def game():
    return 446 #this value change in txt file

score = game()
with open("highscore.txt") as f:
    highscore = int(f.read())

if highscore:
    with open("highscore.txt", "w") as f:
        f.write(str(score))
'''

#Some modification in above programme
def game():
    return 4464

#This Value Change In txt file

score = game()
with open("highscore.txt") as f:
    highscore = (f.read())

if highscore=='':
    with open("highscore.txt",'w') as f:
        f.write(str(score))

elif int(highscore)<score:
    with open("highscore.txt", "w") as f:
        f.write(str(score))

