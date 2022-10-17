from art import logo
from replit import clear

#Calculator 
def Add(n1, n2):
  return n1 + n2

def Subtract(n1, n2):
  return n1 - n2

def Multiply(n1, n2):
  return n1 * n2

def Divide(n1, n2):
  return n1 / n2

operations = {
  "+" : Add,
  "-" : Subtract,
  "*" : Multiply,
  "/" : Divide,
}

def calculator():
  print(logo)
  num1 = float(input("What is the first number: "))
  
  for key in operations:
    print(key)
  more_operation = True
  while more_operation:
    op_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number: "))
    calculation_function = operations[op_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {op_symbol} {num2} = {answer}")
    user_decides = input(f"Type 'y' to continue calculating with {answer}, 'n' to start a new calculation, or 'x' to exit: ")
    if user_decides == "y":
      num1 = answer
    elif user_decides == "n":
      clear()
      calculator()
    else:
      print("Goodbye!")
      more_operation = False

calculator()