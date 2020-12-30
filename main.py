#Calculator

from art import logo

#Add
def add(n1, n2):
  return n1 + n2
#Subtract
def subtract(n1, n2):
  return n1 - n2
#Multiply
def multiply(n1, n2):
  return n1 * n2
#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/" : divide
  }

def calculator():
  print(logo)

  num1 = float(input("What's the first number?\n"))

  for key in operations:
      print(key)

  should_continue = True

  while should_continue:

    operation_key = input("Pick an operation from the line above: ")

    num2 = float(input("What's the next number?\n"))

    operation_value = operations[operation_key]
    answer = operation_value(num1, num2)
    print(f"{num1} {operation_key} {num2} = {answer}")

    num1 = answer

    more_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
    if more_calculation == "n":
      should_continue = False
      calculator()

calculator()