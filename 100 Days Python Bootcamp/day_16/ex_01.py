from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('chocolate')
timmy.fd(100)
print(timmy)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ['George', 'Jack', 'Alex'])
table.add_column("Type", ['Tall', 'Strange', 'Smelly'])
table.align = 'l'
print(table)