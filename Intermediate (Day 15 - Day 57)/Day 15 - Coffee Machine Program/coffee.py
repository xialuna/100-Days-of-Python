from data import MENU, resources, menuList, receipt
earnings = 0.0
def report():
    print(f"\033[35m\nWater: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: ₱ {earnings}\n\033[0m")

def calculateCoins():
    print("\x1B[3m"+"Please Insert Coins..."+"\x1B[0m")
    total = int(input("Number of ₱20 coins: ")) * 20
    total += int(input("Number of ₱10 coins: ")) * 10
    total += int(input("Number of ₱5 coins: ")) * 5
    total += int(input("Number of ₱1 coins: ")) 
    total += int(input("Number of ₱25 centavos: "))  * 0.25
    return total

def checkResource (ingredients):
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"\033[31m\nSorry we are currently out of {item}\033[0m")
            return False
        else:
            return True

def makeCoffee(ingredients, coffee):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"\033[32mYour {coffee} is ready. Enjoy!☕️\033[0m")  


while True:
    print(menuList)
    command = input("Enter command: ").lower()

    if command == "report":
        report()
        if input("\x1B[3m"+"Press enter to exit report: "+"\x1B[0m") == '\n':
            continue
    elif command == "off":
        break
    else:
        drink= "espresso" if command == "1" else ("latte" if command == "2" else "cappuccino")
        coffee = MENU[drink]
        if checkResource(coffee["ingredients"]) == True:
            cash = calculateCoins()
            total = coffee["cost"]
            if cash >= total:
                change = round(cash - total,2)
                earnings += total
                receipt(total,cash,change)
                makeCoffee(coffee["ingredients"],drink)
            else:
                print("\033[31m\nSorry that's not enough money. Money refunded\033[0m")

print("\x1B[3m"+"Shutting down coffee machine..."+"\x1B[0m")

            
                
            


        

        



