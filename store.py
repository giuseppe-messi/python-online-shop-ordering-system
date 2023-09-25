from category import Category
from item import Item
from utils import handle_operation_errors, is_valid_category, is_valid_item_info


class Store:
    def __init__(self):
        self.categories = {}
        self.items = {}

    @handle_operation_errors
    def add_category(self, name):
        is_valid_category(name)
        if name in self.categories:
            raise ValueError(f"Category {name} already exists!")

        self.categories[name] = Category(name)
        print(f"Category {name} added successfully!")

    @handle_operation_errors
    def add_item(self, item_info):
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
            print(f"Item: {item.name} added successfully!")
        else:
            raise ValueError(f"Category: {product_category} does not exist.")

    @handle_operation_errors
    def get_item_by_id(self, item_id):
        item = self.items.get(item_id)
        if not item:
            raise KeyError(f"Item with id: {item_id} does not exist!")

        return item

    @handle_operation_errors
    def delete_item(self, id):
        if id in self.items:
            del self.items[id]
            print(f"Item with id: {id} removed from store!")
        else:
            raise KeyError(f"Item with id: {id} removed from order!")
