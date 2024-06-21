# Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

# Example Input
# 56
# Example Output
# You have 1768 weeks left.

# life left
age = input()
years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left.")

# ALTERNATIVE METHOD...//////

MAX_AGE = 90
MONTHS_IN_YEAR = 12
WEEKS_IN_YEAR = 52
DAYS_IN_YEAR = 365

age = int(input("What is your age?\n>> "))
years_left = MAX_AGE - age
months_left = years_left * MONTHS_IN_YEAR
weeks_left = years_left * WEEKS_IN_YEAR
days_left = years_left * DAYS_IN_YEAR

print(f"You have {years_left} years left; {months_left} months left;"
      f" {weeks_left} weeks left or {days_left} days left to live, approximately.")