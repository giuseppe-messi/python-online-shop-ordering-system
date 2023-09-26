navigate to the project root directory in the terminal
open the python interpreter:

```
python3
```

then open and execute the store, customer and payment class:

exec(open("store.py").read())
exec(open("customer.py").read())
exec(open("payment.py").read())

and import util functions:

from utils import print_store_matrix, create_items_matrix

from this point you can interact with the program
calling all the methods available to you to create an online store

create instance of a store
store = Store()

use the helper function to print the store items
in a table, it helps visualise the store state
I incourage you to call this function at any given time you like

print_store_matrix(create_items_matrix(store))

use the add_category and add_item methods to start populating the store
I incourage you to call these methods with non string arguments to see error handling in action

accepted category:

store.add_category("technology")
store.add_category("kitchen")

not accepted category:

store.add_category("")
store.add_category(3456)
store.add_category(True)

well formatted item:

store.add_item(
{
"id": 1,
"name": "phone",
"price": 10,
"stock": 2,
"product_category": "technology",
}
)

a badly formatted item instead, would have one of the mandatory values missing
or if some of the values have an unexpected type or if that item id alreadt exist

let's add a few more and print the store table!!!

store.add_item(
{"id": 2, "name": "spoons", "price": 8, "stock": 4, "product_category": "kitchen"}
)

store.add_item(
{"id": 3, "name": "TV", "price": 800, "stock": 22, "product_category": "technology"}
)

store.add_item(
{
"id": 4,
"name": "speakers",
"price": 200,
"stock": 6,
"product_category": "technology",
}
)

print_store_matrix(create_items_matrix(store))

you can also delete and item by its id
ex: store.delete_item(1)

After the store has been populated, we can create customers!

giuseppe = Customer(
store,
{
"name": "giuseppe",
"surname": "messiga",
"email": "email@email.com",
"address": "12 address, London, N89RU",
},
)

now, via the order class inside the customer instance, you can add and delete items by id, and view the order
the item has to exist otherwise an error happens

giuseppe.order.add_item(1)
giuseppe.order.add_item(4)
giuseppe.order.view_order()

then we create a payment instance, which takes a customer as only argument and call the make_payment method:

payment_giuseppe = Payment(giuseppe)
payment_giuseppe.make_payment()

Thanks! I hope you enjoyed my simple online shopping system!
