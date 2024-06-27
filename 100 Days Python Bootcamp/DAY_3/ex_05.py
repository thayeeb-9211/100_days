# pizza order

# Based on a user's order, work out their final bill.
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

# Example Input
# L
# Y
# N
# Example Output
# Thank you for choosing Python Pizza Deliveries!
# Your final bill is: $28.

print("Thank you for choosing Python Pizza Deliveries!")
size = input().lower() # What size pizza do you want? s, m, or l
add_pepperoni = input().lower() # Do you want pepperoni? y or n
extra_cheese = input().lower() # Do you want extra cheese? y or n

bill = 0
if size == "s":
  bill += 15
if size == "m":
  bill += 20
if size == "l":
  bill += 25

if add_pepperoni == "y":
  if size == "s":
    bill += 2
  else:
    bill += 3

if extra_cheese == "y":
  bill += 1

print(f"Your final bill is: ${bill}.")
