# turtle racers

from turtle import Turtle, Screen
from random import choice, randint

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']


class Racer(Turtle):

    def __init__(self, lane):
        Turtle.__init__(self)
        self.shape('turtle')
        self.color(COLORS[lane])
        self.penup()
        self.setpos(-200, -120 + 35 * lane)

    def move(self):
        self.fd(randint(1, 10))


class RaceTurtles:

    def __init__(self):
        self.racers = []
        self.generate_racers()
        self.winner = None

    def generate_racers(self):

        self.racers = [Racer(lane) for lane in range(7)]

    def race(self):

        racing = True
        while racing:
            racer = choice(self.racers)
            racer.move()
            if racer.xcor() > 200:
                self.winner = racer.color()[1]
                racing = False


screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Racers")
bet_choice = screen.textinput(title="Make your bet", prompt="Which turtle "
                                                            "will win the race? Enter a color: ")
race = RaceTurtles()
race.race()
if bet_choice == race.winner:
    screen.textinput(title=f"The winner is {race.winner}", prompt="Congratulations! You win!")
else:
    screen.textinput(title="Sorry", prompt=f"You lose, the winner was {race.winner}")

screen.exitonclick()
