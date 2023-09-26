# Welcome to my online shop ordering system in Python!

The following is just a flow example on how to populate the store with categories and items and how a customer can add items to their order and then make a payment.

Following this example are detailed descriptions of each class used to create this project!

<br>

### How to use this program:

Navigate to the project root directory in the terminal and open the Python interpreter:

```
python3
```

In order to properly run the program from the interpreter, we need to import some files; open and execute the store, customer and payment class:

```
exec(open("store.py").read())
exec(open("customer.py").read())
exec(open("payment.py").read())
```

Also, import some utility functions:

```
from utils import print_store_matrix, create_items_matrix
```

---

From this point, you can interact with the program, calling all the methods available to create an online store.

---

Create an instance of a store.

```
store = Store()
```

Use the helper function to print the store items in a table format; it helps visualise the store state. I encourage you to call this function at any given time.

```
print_store_matrix(create_items_matrix(store))
```

Use the `add_category` and `add_item` methods to populate the store.
I encourage you to call these methods with non-string arguments to see the error handling.

#### accepted category:

```
store.add_category("technology")
store.add_category("kitchen")
```

#### not accepted category:

```
store.add_category("")
store.add_category(3456)
store.add_category(True)
```

#### well-formatted item:

```Python
store.add_item({
    "id": 1,
    "name": "phone",
    "price": 10,
    "stock": 2,
    "product_category": "technology",
})
```

A poorly formatted item would have one of the mandatory values missing, some of the values have an unexpected type, or that item ID already exists.

#### Let's add a few more and print the store table!!!

```Python
store.add_item({
    "id": 2, "name":
    "spoons",
    "price": 8,
    "stock": 4,
    "product_category": "kitchen"
})

store.add_item({
    "id": 3,
    "name": "TV",
    "price": 800,
    "stock": 22,
    "product_category": "technology"
})

store.add_item({
    "id": 4,
    "name": "speakers",
    "price": 200,
    "stock": 6,
    "product_category": "technology",
})


print_store_matrix(create_items_matrix(store))
```

you can also delete an item by its id
ex: `store.delete_item(1)`

After the store has been populated, we can create a customer!

```Python
giuseppe = Customer(
    store,
    {
    "name": "giuseppe",
    "surname": "message",
    "email": "email@email.com",
    "address": "12 address, London, N89RU",
    },
)
```

Now, via the `order` class inside the customer instance, you can add and delete items by ID and view the order; the item has to exist; otherwise, an error will happen.

```
giuseppe.order.add_item(1)
giuseppe.order.add_item(4)
giuseppe.order.view_order()
```

Then we create a payment instance, which takes a customer as its only argument and calls the `make_payment` method:

```
payment_giuseppe = Payment(giuseppe)
payment_giuseppe.make_payment()
```

<br>

## Classes

Detailed description of each class used in this project!

#### Store Class

| Properties/Methods      | Description                                          |
| ----------------------- | ---------------------------------------------------- |
| categories              | A dictionary to store categories as key-value pairs. |
| items                   | A dictionary to store items as key-value pairs.      |
| add_category(name)      | Method to add a new category to the store.           |
| add_item(item_info)     | Method to add a new item to the store.               |
| get_item_by_id(item_id) | Method to retrieve an item by its ID.                |
| delete_item(id)         | Method to delete an item from the store by its ID.   |

#### Category Class

| Properties/Methods | Description                                               |
| ------------------ | --------------------------------------------------------- |
| name               | Property to store the name of the category.               |
| items              | A dictionary to store items within the category.          |
| add_item(item)     | Method to add an item to the category's items dictionary. |

#### Item Class

| Properties/Methods | Description                                 |
| ------------------ | ------------------------------------------- |
| id                 | Property to store the ID of the item.       |
| name               | Property to store the name of the item.     |
| price              | Property to store the price of the item.    |
| product_category   | Property to store the category of the item. |

#### Customer Class

| Properties/Methods | Description                                                                    |
| ------------------ | ------------------------------------------------------------------------------ |
| store              | Property to store a reference to the store.                                    |
| name               | Property to store the customer's name.                                         |
| surname            | Property to store the customer's surname.                                      |
| email              | Property to store the customer's email address.                                |
| address            | Property to store the customer's address.                                      |
| order              | Property to store an instance of the Order class associated with the customer. |

#### Order Class

| Properties/Methods   | Description                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------- |
| customer             | Property to store a reference to the customer associated with the order.                    |
| store                | Property to store a reference to the store associated with the order.                       |
| items                | A dictionary to store items in the order.                                                   |
| add_item(item_id)    | Method to add an item to the order by item ID.                                              |
| get_total_price()    | Method to calculate and return the total price of the items in the order.                   |
| view_order()         | Method to display the contents of the order, including item names, prices, and total price. |
| remove_item(item_id) | Method to remove an item from the order by item ID.                                         |
| clear_order()        | Method to clear all items from the order.                                                   |

#### Payment Class

| Properties/Methods | Description                                                                |
| ------------------ | -------------------------------------------------------------------------- |
| customer           | Property to store a reference to the customer associated with the payment. |
| order              | Property to store a reference to the customer's order.                     |
| make_payment()     | Method to process a payment for the customer's order.                      |

<br>

## Utility Functions

Description of utility functions used in the program!

| Function Name                    | Description                                                                                                                                                                                    |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| handle_operation_errors(method)  | A decorator function that catches common error types (TypeError, ValueError, KeyError) when calling other functions and prints error messages if they occur.                                   |
| is_valid_category(name)          | Validates that the input name is a non-empty string and raises errors for invalid input types or empty names.                                                                                  |
| is_valid_item_info(item_info)    | Validates the structure of item information in the item_info dictionary, checking for required fields and their data types.                                                                    |
| is_valid_customer(customer_info) | Validates the structure of customer information in the customer_info dictionary, checking for required fields and their data types.                                                            |
| print_store_matrix(matrix)       | Formats and prints a tabular matrix, adjusting column widths to align data neatly. It includes a header row, a separator, and content rows.s                                                   |
| create_items_matrix(store)       | Generates a matrix (2D list) representing item information in a store, including item name, stock, price, category, and ID. This matrix can be used for tabular display or further processing. |

<br>

### Thanks! I hope you enjoyed my simple online shopping system!
