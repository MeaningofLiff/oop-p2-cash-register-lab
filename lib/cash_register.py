#!/usr/bin/env python3
#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity):
        # Add to total
        self.total += price * quantity

        # Add item to items list
        self.items.append(item)

        # Record transaction
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        # Spec: If no transactions print message
        if len(self.previous_transactions) == 0:
            print("There is no discount to apply.")
            return self.total

        # Apply percentage discount
        self.total = self.total - (self.total * (self.discount / 100))
        return self.total

    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            return

        last = self.previous_transactions.pop()

        # Subtract last transaction from total
        self.total -= last["price"] * last["quantity"]

        # Remove matching item
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == last["item"]:
                self.items.pop(i)
                break
 