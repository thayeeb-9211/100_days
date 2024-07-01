from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("+"))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()

    
    



# alternate_method...................
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operands = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

answer = 0
new_calc = 'n'
while True:
    if new_calc == 'n':
        num1 = int(input("What is your first number?\n>> "))
    else:
        num1 = answer
        print(f"First number is: {num1}")
    if num1 == 'exit': break
    for operand in operands:
        print(operand)
    operand = input("Pick an operation:\n>> ")
    num2 = int(input("What is your next number?\n>> "))
    answer = operands[operand](num1, num2)
    print(f"{num1} {operand} {num2} = {answer}")
    new_calc = input(f"Type 'y' to continue with {answer}, or type 'n' to start new calculation:\n>> ")