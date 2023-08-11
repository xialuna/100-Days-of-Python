import os
from calcuLogo import logo
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operation = {"+": add,
             "-": subtract,
             "*": multiply,
             "/": divide,
             }

choice = 2
while True: #You can also use recursive function instead of a while loop
  if choice == 2:
    os.system('cls')
    print(logo)
    print("Instruction: operation for calculator includes: ", end ="")
    for sign in operation:
        print(f"[{sign}] ",end="")
    n1 = float(input("\n\nEnter first number: "))
  symbol = input("Operation Symbol: ")
  n2 = float(input("Enter next number: "))

  result = operation[symbol](n1,n2)
  print(f"\033[32m{n1} {symbol} {n2} = {result}\033[0m")

  choice = int(input(f"\nContinue calculating \033[32m'{result}'\033[0m?\n\t[1] Yes\n\t[2] Start New Calculation\nEnter Choice: "))
  if choice == 1:
      n1 = result
      print()