# treasure map


# You are going to write a program that will mark a spot on a map with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what it looks like, notice the nesting:
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
# This is a bit hard to work with. So on lines 6 and 23, 
# we've used this line of code print(f"{line1}\n{line2}\n{line3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# Now it looks a bit more like the coordinates of a real map:
# Your job is to write a program that allows you to mark a square on the map using a letter-number system.
# So an input of A3 should place an X at the position shown below:
# First, your program must take the user input and convert it to a usable format.
# Next, you need to use that input to update your nested list with an "X". Remember that your nested list map actually looks like this:
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
# Example Input 1
# B3
# Example Output 1
# Hiding your treasure! X marks the spot.
# ['⬜️', '️⬜️', '️⬜️']
# ['⬜️', '⬜️', '️⬜️']
# ['⬜️️', 'X', '⬜️️']
# Example Input 2
# B1
# Example Output 2
# Hiding your treasure! X marks the spot.
# ['⬜️', 'X', '️⬜️']
# ['⬜️', '⬜️', '️⬜️']
# ['⬜️️', '⬜️️', '⬜️️']


line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

letter = position[0].lower()
abc = ["a","b","c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "x"

print(f"{line1}\n{line2}\n{line3}")

# alternative_method....

def show_map():
    print(f"{row1}\n{row2}\n{row3}\n")

row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

map = [row1, row2, row3]
show_map()


position = input("Where do you want to put the treasure?")
column, row = int(position[0]), int(position[1])
map[column - 1][row - 1] = 'X'

show_map()