#Object Oriented Programming:
'''
class Phone:
    def make_call(self):
        print("Making Phone call to the person which would you like to chat")
    def play_game(self):
        print("Playing Game which would you like to play")

p1 = Phone() #Object

p1.make_call()
p1.play_game()'''

#Using input from user
class Phone:
    def set_colour(self,colour):
        self.colour=colour

    def set_cost(self,cost):
        self.cost=cost

    def show_colour(self):
        print(self.colour)

    def show_cost(self):
        print(self.cost)

    def make_call(self):
        print("Making phone call")

    def play_game(self):
        print("Playing Game")

p1 = Phone()
p1.set_colour('blue')
p1.set_cost(300)

p1.show_colour()
p1.show_cost()
