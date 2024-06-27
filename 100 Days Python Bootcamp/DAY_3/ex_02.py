
print("Welcome to the rollercoaster")
height = int(input("Whats is your height in cm?\n>> "))
age = int(input("How old are you?\n>> "))

bill = 0
if height >= 120:
    if age >= 45 and age <= 55:
        print("Midlife Crisis special - free ride!")
    elif age >= 18:
        print("Adult tickets £12")
        bill = 12
    elif age >= 12:
        print("Youth tickets £7")
        bill = 7
    else:
        print("Child tickets £5")
        bill = 5
    photo = input("Do you want a photo of your ride y/n?\n>> ")
    if photo == 0:
        print("Photos cost £3")
        bill += 3
    print("Your bill is £{bill} Enjoy the ride!")
else:
    print("Sorry, you are not tall enough to ride.")