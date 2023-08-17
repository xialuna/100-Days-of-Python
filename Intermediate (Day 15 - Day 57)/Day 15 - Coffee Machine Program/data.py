MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 50.25,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 125.0 ,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 200.75 ,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

menuList ='''\033[33m
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃       Coffee Menu        ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ [1] Espresso             ┃
┃     Price: ₱50.25        ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ [2] Caramel Latte        ┃
┃     Price: ₱125.0        ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ [3] Cappuccino           ┃
┃     Price: ₱200.75       ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛
\033[0m'''

def receipt(total,cash,change):
    print('''\033[35m
  Total:           ₱ %.2f
  Cash:            ₱ %.2f
────────────────────────────
  Change: ₱ %.2f 
\033[0m'''%(total,cash,change))
    