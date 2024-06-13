def make_payment (self, cost):
    """Returns True when payment is accepted, or Flase if insufficient."""
    self.process_coins()
    if self.money_received >= cost:
        change = round(self.money_received-cost,2)
        print(f"Here is {self.CURRENCY}{change} in change.")
        self.profit += Cost
        self.money_received = 0
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
    self.money_received = 0
        return False
make_payment()
