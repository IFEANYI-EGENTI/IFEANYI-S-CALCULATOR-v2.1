### IFEANYI EGENTI
print("IFEANYI'S CALCULATOR v2.1")
print()

import math

def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def division(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero"
    return num1 / num2
def exponentiation(num1, num2):
    return num1 ** num2
def square_root(num):
    if num < 0:
        print()
        return "Error: Cannot calculate square root of a negative number"
    print()
    return num ** 0.5
def logarithm(num):
    if num <= 0:
        print()
        return "Error: Cannot calculate logarithm of a non-positive number"
    print()
    return math.log(num)



class Calculator:
  def __init__(self):
    self.operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}

  def add_operation(self, symbol, function):
    self.operations[symbol] = function
    
  def calculate(self, num1, symbol, num2=None):
    if not isinstance(num1, (int, float)):
        raise TypeError("Input must be a number")
    if symbol not in self.operations:
        raise ValueError("Invalid Operator. Please use +, -, *, /, expo, sqrt, log")
    if num2 is None:
        return self.operations[symbol](num1)   # single argument
    return self.operations[symbol](num1, num2) # two arguments


calc = Calculator()
calc.add_operation("expo", exponentiation)
calc.add_operation("sqrt", square_root)
calc.add_operation("log", logarithm)                      

while True:
    try:
        print()
        print()
        first_number = float(input("Please input your first digit: "))
        symbol = input("Please enter an operator (+, -, *, /, expo, sqrt, log): ")
        if symbol in ("sqrt", "log"):
            result = calc.calculate(first_number, symbol)
        else:
            second_number = float(input("Please input your second digit: "))
            print()
            result = calc.calculate(first_number, symbol, second_number)
    except (ValueError, TypeError, OverflowError) as e:
        print("Error:", e)
        continue
    if isinstance(result, str):
          print(result)
    else:
        print(int(result) if result == int(result) else result)
    print()
    print()
    print(("Do you want to use Calculator again?"))
    again = input("Input 'yes' to use Calculator again or 'no' to exit: ")
    if again != "yes":
        break