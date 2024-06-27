### Project 1: Basic Calculator

# **Description:** Create a simple calculator that performs basic arithmetic operations: addition, subtraction, multiplication, and division.

#### Hints and TODOs:

# 1. **Define Function**: Write a function operation for `add`, `subtract`, `multiply`, and `divide`.
# 2. **Main Function**: Create a main function that takes user input and calls the appropriate function based on the operation

def operation(a, b):
    # Define operations
    add = a + b
    sub = a - b
    mul = a * b
    if b == 0:
        return "Error! Division by zero."
    else:
        div = a / b
    
    choice = input("Enter choice (1/2/3/4/5): ")

    while True:
        # TODO: Validate input
        if choice == '1':
            print(f"Result: {add}")
            break
        elif choice == '2':
            print(f"Result: {sub}")
            break
        elif choice == '3':
            print(f"Result: {mul}")
            break
        elif choice == '4':
            print(f"Result: {div}")
            break
        elif choice == '5':
            print("Exiting the program.")
            break

# Display operation choices
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

# Take user input for numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Call main function
operation(a = num1, b = num2)
