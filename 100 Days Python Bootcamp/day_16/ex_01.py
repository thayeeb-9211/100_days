# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.fd(100)
# print(timmy)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Charmander","Fire"])
table.add_row(["Squiritle", "water"])
table.align = 'l'
print(table)
