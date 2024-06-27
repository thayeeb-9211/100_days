#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill?"))
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)

# print(f"each person should pay:${final_amount}")

while True:
    print("\nWelcome to the tip calculator...!")
    bill  = float(input("what was the total bill?$: \n"))
    tip  = int(input("How much tip would you like to give? 10, 12 or 15 $: \n"))
    people = int(input("How many people to spit the bill?: \n"))
  
    total_bill = bill + (bill * (tip / 100))
    final_bill  = round((total_bill/people), 2)
  
    print(f"bill_per_person: {final_bill}")