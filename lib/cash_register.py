#!/usr/bin/env python3
#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        # Increase total
        self.total += price * quantity

        # Add items, including multiples
        for _ in range(quantity):
            self.items.append(item)

        # Record transaction
        self.previous_transactions.append(
            {"item": item, "price": price, "quantity": quantity}
        )

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total -= self.total * (self.discount / 100)

        # Format exactly as tests expect
        if float(self.total).is_integer():
            total_str = str(int(self.total))
        else:
            total_str = f"{self.total:.2f}"

        print(f"After the discount, the total comes to ${total_str}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last = self.previous_transactions.pop()

        # Subtract from total
        self.total -= last["price"] * last["quantity"]

        # Remove items (including multiples)
        for _ in range(last["quantity"]):
            for i in range(len(self.items) - 1, -1, -1):
                if self.items[i] == last["item"]:
                    self.items.pop(i)
                    break
 