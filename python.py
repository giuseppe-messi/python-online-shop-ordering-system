class Store:
    def __init__(self):
        self.categories = {}
        self.items = {}

    def add_category(self, name):
        self.categories[name] = Category(name)

    def add_item(self, item_data):
        category = item_data.get('category')
        id = item_data.get('id')
        category = self.categories.get(category)
        if (category):
            item = Item(item_data)
            category.add_item(item)
            self.items[id] = item
        else:
            print("Category: {} does not exist.".format(category))

    def delete_item(self, id):
        item = self.items[id]
        if (item):
            del item

    def get_item_by_id(self, item_id):
        item = self.items[item_id]
        if (item):
            return item
        else:
            print("Item does not exist!")


class Category:
    def __init__(self, name):
        self.name = name
        self.items = {}

    def add_item(self, item):
        self.items[item.id] = item


class Item:
    def __init__(self, item_data):
        self.id = item_data.get('id')
        self.name = item_data.get('name')
        self.price = item_data.get('price')
        self.stock = item_data.get('stock')
        self.category = item_data.get('category')

    def reduce_stock(self):
        self.stock -= 1
        # will need to remove complete from stock if it's already at 0


class Customer:
    def __init__(self, name, surname, email, address, customer_id, store):
        self.name = name
        self.surname = surname
        self._email = email
        self._address = address
        self.customer_id = customer_id
        self.store = store
        self.order = Order(self, store)


class Order:
    def __init__(self, customer, store):
        self.customer = customer
        self.store = store
        self.items = {}

    def add_item(self, item_id):
        item = store.get_item_by_id(item_id)
        if (not item):
            print("Item not found!")
        elif (item.stock == 0):
            print("This item has run out!")
        else:
            self.items[item_id] = item

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
        print('Sucess! You just bought: bla for {}'.format(
              self.order.get_total_price()))

        for item in self.order.items.values():
            item.reduce_stock()

        self.order.clear_order()


store = Store()
store.add_category('technology')
store.add_category('health')
store.add_category('kitchen')

store.add_item({
    'id': 1,
    'name': 'phone',
    'price': 10,
    'stock': 2,
    'category': 'technology'
})

store.add_item({
    'id': 2,
    'name': 'spoons',
    'price': 8,
    'stock': 4,
    'category': 'kitchen'
})
# store.add_item(3, 'glasses', 5, 1,  'kitchen')
# store.add_item(4, 'knives', 12, 5, 'kitchen')
# store.add_item(5, 'laptop', 200, 4, 'technology')
# store.delete_item(5)
# store.delete_item(1)

customer = Customer('giuseppe', 'messiga', 'email@email.com',
                    '12 address, London, N89RU', 1, store)

customer.order.add_item(1)
customer.order.add_item(2)

for item in store.items.values():
    print(vars(item))

# print(len(customer.order.items))


payment = Payment(customer)
payment.make_payment()

for item in store.items.values():
    print(vars(item))

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
#         'name': item.name,
#         'category': item.category.name,
#         'id': item.id,
#     }
#     print(item_values)
