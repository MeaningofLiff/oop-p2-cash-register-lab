class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, int) or value < 0 or value > 100:
            print("Not valid discount")
            return
        self._discount = value

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.total == 0:
            print("There is no discount to apply.")
            return

        if self.discount > 0:
            self.total = self.total - (self.total * (self.discount / 100))

        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            return

        last = self.previous_transactions.pop()
        item = last["item"]
        price = last["price"]
        quantity = last["quantity"]

        self.total -= price * quantity

        removed = 0
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == item:
                self.items.pop(i)
                removed += 1
                if removed == quantity:
                    break
