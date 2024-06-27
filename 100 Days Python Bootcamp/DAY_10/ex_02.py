# days in month calculator
# \
#     Convert the is_leap() functtion
# In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

# Create a new function called days_in_month()
# You are then going to modify a function called days_in_month() which will take a year and a month as inputs, e.g.

# days_in_month(year=2022, month=2)
# And it will use this information to work out if the year is a leap year and decide the number of days in the month, then return that as the output, e.g.:

# 28
# The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.

# Hint
# Look at the function call at the bottom of the code to see the positional arguments. The order is very important.

# Feel free to choose your own parameter names.

# Remember that month_days is a List and Lists in Python start at position 0. So the number of days in January is month_days[0]

# Be careful with indentation.

def is_leap(year):
    """determines if a year is a leap year int -> boolean"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):

    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year):
        days[1] = 29
    return days[month - 1]

year = int(input("Which year do you want to check?\n>> "))
month = int(input("Which month do you want to check?\n>> "))
print(days_in_month(year, month))
