class MoneyMachine:

    CURRENCY = "₱"

    COIN_VALUES = {
        "₱20 coins": 20,
        "₱10 coins": 10,
        "₱5 coins": 5,
        "₱1 coin": 1,
        "₱25 centavos": 0.25
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("\n\x1B[3m"+"Please Insert Coins..."+"\x1B[0m")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"Number of {coin}: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"\nHere is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("\nSorry that's not enough money. Money refunded.\n")
            self.money_received = 0
            return False
