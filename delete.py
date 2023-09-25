from store import Store
from category import Category
from item import Item
from customer import Customer
from order import Order
from payment import Payment
from utils import print_store_matrix, create_items_matrix

store = Store()

print_store_matrix(create_items_matrix(store))

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

store.delete_item(1)

print_store_matrix(create_items_matrix(store))

store.add_item(
    {"id": 2, "name": "spoons", "price": 8, "stock": 4, "product_category": "kitchen"}
)
# store.add_item(
#     {"id": 3, "name": "knives", "price": 12, "stock": 2, "product_category": "kitchen"}
# )
print_store_matrix(create_items_matrix(store))

customer = Customer(
    store,
    {
        "name": "giuseppe",
        "surname": "messiga",
        "email": "email@email.com",
        "address": "12 address, London, N89RU",
    },
)

customer.order.add_item(2)
customer.order.add_item(1)


# for item in store.items.values():
#     print(vars(item))

# print(len(customer.order.items))

customer.order.view_order()

customer.order.remove_item(2)

customer.order.view_order()


payment = Payment(customer)
payment.make_payment()

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
