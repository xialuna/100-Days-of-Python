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