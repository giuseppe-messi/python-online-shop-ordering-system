from typing import Dict
from type_definitions import CustomerInfoType, ItemInfoType
from utils import (
    handle_operation_errors,
    is_valid_category,
    is_valid_customer,
    is_valid_item_info,
)


class Store:
    """
    Represents a store that manages categories and items.
    """

    def __init__(self):
        self.categories: Dict[str, Category] = {}
        self.items: Dict[str, Item] = {}

    @handle_operation_errors
    def add_category(self, name: str):
        """
        Add a new category to the store.
        """

        is_valid_category(name)

        if name in self.categories:
            raise ValueError(f"Category {name} already exists!")

        self.categories[name] = Category(name)
        print(f"\n\nCategory {name} added successfully!\n\n")

    @handle_operation_errors
    def add_item(self, item_info: ItemInfoType):
        """
        Add a new item to the store.
        """

        is_valid_item_info(item_info)

        product_category = item_info.get("product_category")
        category = self.categories.get(product_category)

        if category:
            ids = [item.id for item in self.items.values()]
            id = item_info.get("id")
            if id in ids:
                raise ValueError(f"An Item with id: {id} already exist!")

            item = Item(item_info)
            category.add_item(item)
            self.items[id] = item
            print(f"\n\nItem: {item.name} added successfully!\n\n")
        else:
            raise ValueError(f"Category: {product_category} does not exist.")

    @handle_operation_errors
    def get_item_by_id(self, item_id: int):
        """
        Get an item from the store by its ID.
        """

        item = self.items.get(item_id)
        if not item:
            raise KeyError(f"Item with id: {item_id} does not exist!")

        return item

    @handle_operation_errors
    def delete_item(self, id: int):
        """
        Delete an item from the store by its ID.
        """

        if id in self.items:
            del self.items[id]
            print(f"\n\nItem with id: {id} removed from store!\n\n")
        else:
            raise KeyError(f"Item with id: {id} not found!")


class Category:
    """
    Represents a category in the store.
    """

    def __init__(self, name: str):
        self.name = name
        self.items = {}

    def add_item(self, item):
        """
        Add an item to the category.
        """

        self.items[item.id] = item


class Item:
    """
    Represents an item in the store.
    """

    def __init__(self, item_info: ItemInfoType):
        self.id = item_info.get("id")
        self.name = item_info.get("name")
        self.price = item_info.get("price")
        self.product_category = item_info.get("product_category")


class Customer:
    """
    Represents a customer in the store.
    """

    @handle_operation_errors
    def __init__(self, store, customer_info: CustomerInfoType):
        is_valid_customer(customer_info)

        self.store = store
        self.name = customer_info.get("name")
        self.surname = customer_info.get("surname")
        self.__email = customer_info.get("email")
        self.__address = customer_info.get("address")
        self.order = Order(self, store)


class Order:
    """
    Represents a order of a customer.
    """

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


class Payment:
    """
    Represents the payment process for a customer's order.
    """

    def __init__(self, customer):
        self.customer = customer
        self.order = customer.order

    def make_payment(self):
        """
        Process a payment for the customer's order.
        """

        item_list = [item.name for item in self.order.items.values()]

        print(item_list)
        if not self.order.items.values():
            print(
                "\n\nError: Your order is empty. Add items to your order before making a payment!\n\n"
            )
        else:
            item_list = [item.name for item in self.order.items.values()]
            items_string = ", ".join(item_list)
            total = self.order.get_total_price()
            self.order.clear_order()
            print(f"\n\nSucess! You just bought: {items_string} for {total}\n\n")
