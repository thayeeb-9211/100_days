# paint can calculator
# You are painting a wall. The instructions on the paint can says that 1 can of paint can 
# cover 5 square meters of wall. Given a random height and width of wall, calculate how many 
# cans of paint you'll need to buy.

# number of cans = (wall height x wall width) ÷ coverage per can.
# e.g. Height = 2, Width = 4, Coverage = 5

# number of cans = (2 * 4) / 5
#                = 1.6
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

# Example Input
# 3
# 9
# Example Output
# You'll need 6 cans of paint.

import math
def paint_calc(height, width, cover):
  number_of_calc = (height*width)/cover
  rounded_value = math.ceil(number_of_calc)
  print(f"You'll need {rounded_value} cans of paint.")

# Define a function called paint_calc() so the code below works.   

test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#Round upto 2 decimal places.
# round(number,2)

# alternative_method
from math import ceil

def paint_calc(height, width, cover):
    return ceil(height * width / cover)

test_h = int(input("What is the height of the wall (m):\n>> "))
test_w = int(input("What is the width of the wall (m):\n>> "))
coverage = 5

cans_needed = paint_calc(height=test_h, width=test_w, cover=coverage)
print(f"You require {cans_needed} of paint.")
