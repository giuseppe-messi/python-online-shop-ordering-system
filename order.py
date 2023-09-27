from utils import handle_operation_errors


class Order:
    def __init__(self, customer, store):
        self.customer = customer
        self.store = store
        self.items = {}

    @handle_operation_errors
    def add_item(self, item_id: int):
        """
        Add an item to the order by its ID.
        """

        if not isinstance(item_id, int):
            raise ValueError("Item id must be of type number!")

        item = self.store.get_item_by_id(item_id)

        if item:
            self.items[item_id] = item
            print(f"\n\n{item.name} successfully added to your order!\n\n")

    def get_total_price(self):
        """
        Calculate the total price of the items in the order.
        """

        total = sum(item.price for item in self.items.values())
        return total

    def view_order(self):
        """
        View the items in the order and their total price.
        """

        if not self.items.values():
            print("\n\nYour order is empty! Add some items!\n\n")
        else:
            print("\n\nYour order:")

            for item in self.items.values():
                print(f"   - {item.name} at: {item.price}! (id: {item.id})")
            total = self.get_total_price()

            print(f"Total: {total}\n\n")

    @handle_operation_errors
    def remove_item(self, item_id: int):
        """
        Remove an item from the order by its ID.
        """

        if item_id in self.items:
            del self.items[item_id]
            print(f"\n\nItem with id: {item_id} removed from order!\n\n")
        else:
            raise KeyError("Item not found in order!")

    def clear_order(self):
        self.items.clear()
