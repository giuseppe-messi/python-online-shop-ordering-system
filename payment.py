class Payment:
    def __init__(self, customer):
        self.customer = customer
        self.order = customer.order

    def make_payment(self):
        item_list = [item.name for item in self.order.items.values()]

        print(item_list)
        if not self.order.items.values():
            print(
                "Error: Your order is empty. Add items to your order before making a payment!"
            )
        else:
            item_list = [item.name for item in self.order.items.values()]
            items_string = ", ".join(item_list)
            total = self.order.get_total_price()
            self.order.clear_order()
            print(f"Sucess! You just bought: {items_string} for {total}")
