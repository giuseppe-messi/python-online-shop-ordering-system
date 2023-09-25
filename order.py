from utils import handle_operation_errors


class Order:
    def __init__(self, customer, store):
        self.customer = customer
        self.store = store
        self.items = {}

    @handle_operation_errors
    def add_item(self, item_id):
        if not isinstance(item_id, int):
            raise ValueError("Item id must be of type number!")

        item = self.store.get_item_by_id(item_id)
        if item:
            self.items[item_id] = item
            print(f"{item.name} successfully added to your order!")

    def get_total_price(self):
        total = sum(item.price for item in self.items.values())
        return total

    def view_order(self):
        if not self.items.values():
            print("Your order is empty! Add some items!")
        else:
            print("Your order:")
            for item in self.items.values():
                print(f"   - {item.name} at: {item.price}! (id: {item.id})")
            total = self.get_total_price()
            print(f"Total: {total}")

    @handle_operation_errors
    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            print(f"Item with id: {item_id} removed from order!")
        else:
            raise KeyError("Item not found in order!")

    def clear_order(self):
        self.items.clear()
