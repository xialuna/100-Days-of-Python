from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
while True:
  print(menu.print_menu())
  command = input("Enter command: ").lower()
  

  if command == "report":
    coffee_maker.report()
    money_machine.report()
  elif command == "off":
    break;
  else:
    drink = menu.find_drink(command)
    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
      coffee_maker.make_coffee(drink)
print("\x1B[3m"+"Shutting down coffee machine..."+"\x1B[0m")


