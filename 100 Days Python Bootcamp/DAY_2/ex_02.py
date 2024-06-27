# BMI Calculator

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# BMI 

# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):


# Example Input 1
# 1.75
# 80
# means: weight = 80 and height = 1.75

# Example Output 1
# 26
# Since: 80 ÷ (1.75 x 1.75) = 26.122448979591837

height = input()
weight = input()
# Your code below this line 👇
weight_as_int = int(weight)
height_as_float = float(height)
# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
print(bmi_as_int)

# ALTERNATIVE METHOD...//////

height = float(input("Enter your height (m):\n>> "))
weight = int(input("Enter your weight (kg):\n>> "))

bmi = int(weight / height ** 2)

print(f"Your BMI is {bmi}")

