from utils import print_store_matrix, create_items_matrix
import validation


class Store:
    def __init__(self):
        self.categories = {}
        self.items = {}

    def add_category(self, name):
        try:
            validation.is_valid_category(name)
            if name in self.categories:
                raise ValueError("Category {} already exists!".format(name))
            else:
                self.categories[name] = Category(name)
                print("Category {} added successfully!".format(name))
        except (TypeError, ValueError) as e:
            print("Error: {}".format(e))

    def add_item(self, item_info):
        try:
            validation.is_valid_item_info(item_info)

            product_category = item_info.get("product_category")
            category = self.categories.get(product_category)

            if category:
                id = item_info.get("id")
                item = Item(item_info)
                category.add_item(item)
                self.items[id] = item
            else:
                raise ValueError(
                    "Category: {} does not exist.".format(product_category)
                )
        except (KeyError, TypeError, ValueError) as e:
            print("Error: {}".format(e))

    def get_item_by_id(self, item_id):
        return self.items[item_id]

    def delete_item(self, id):
        item = self.items[id]
        if item:
            del item


class Category:
    def __init__(self, name):
        self.name = name
        self.items = {}

    def add_item(self, item):
        self.items[item.id] = item


class Item:
    def __init__(self, item_info):
        self.id = item_info.get("id")
        self.name = item_info.get("name")
        self.price = item_info.get("price")
        self.stock = item_info.get("stock")
        self.product_category = item_info.get("product_category")

    def reduce_stock(self):
        self.stock -= 1
        # will need to remove complete from stock if it's already at 0


class Customer:
    def __init__(self, store, customer_info):
        try:
            validation.is_valid_customer(customer_info)

            self.store = store
            self.name = customer_info.get("name")
            self.surname = customer_info.get("surname")
            self.email = customer_info.get("email")
            self.address = customer_info.get("address")
            self.order = Order(self, store)

        except (KeyError, TypeError, ValueError) as e:
            print("Error: {}".format(e))


class Order:
    def __init__(self, customer, store):
        self.customer = customer
        self.store = store
        self.items = {}

    def add_item(self, item_id):
        print("HERE")

        try:
            item = store.get_item_by_id(item_id)

            if not item:
                raise ValueError("Item with id: {} does not exist!".format(item_id))

            if item.stock == 0:
                print("This item has run out!")
            else:
                self.items[item_id] = item

        except ValueError as e:
            print("in error")
            print("Error: {}".format(e))

    def get_total_price(self):
        total = sum(item.price for item in self.items.values())
        return total

    def clear_order(self):
        self.items.clear()


class Payment:
    def __init__(self, customer):
        self.customer = customer
        self.order = customer.order

    def make_payment(self):
        print(
            "Sucess! You just bought: bla for {}".format(self.order.get_total_price())
        )

        for item in self.order.items.values():
            item.reduce_stock()

        self.order.clear_order()


store = Store()


store.add_category("")
store.add_category(3456)
store.add_category(True)
store.add_category("technology")
store.add_category("health")
store.add_category("kitchen")


store.add_item(
    {
        "id": 1,
        "name": "phone",
        "price": 10,
        "stock": 2,
        "product_category": "technology",
    }
)

print_store_matrix(create_items_matrix(store))

# store.add_item(
#     {"id": 2, "name": "spoons", "price": 8, "stock": 4, "product_category": "kitchen"}
# )
# store.add_item(
#     {"id": 3, "name": "knives", "price": 12, "stock": 2, "product_category": "kitchen"}
# )
customer = Customer(
    store,
    {
        "name": "giuseppe",
        "surname": "messiga",
        "email": "email@email.com",
        "address": "12 address, London, N89RU",
    },
)

customer.order.add_item(3)
# customer.order.add_item(2)


# for item in store.items.values():
#     print(vars(item))

# print(len(customer.order.items))


# payment = Payment(customer)
# payment.make_payment()


# print(len(customer.order.items))


# Print category names

# for category in store.categories.values():
#     category_values = {
#         'name': category.name,
#         'items': [item.name for item in category.items.values()],
#         'id': category.id,
#     }
#     print(category_values)

# Print items names
# for item in store.items.values():
#     item_values = {
#         "name": item.name,
#         "category": item.product_category,
#         "id": item.id,
#     }
#     print(item_values)
