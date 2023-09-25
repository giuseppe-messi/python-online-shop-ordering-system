def handle_operation_errors(method):
    def wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except (TypeError, ValueError, KeyError) as e:
            print("Error: {}".format(e))

    return wrapper


def is_valid_category(name):
    if not isinstance(name, str):
        raise TypeError("Category name must be a string!")
    if not name:
        raise ValueError("Category name cannot be empty!")


def is_valid_item_info(item_info):
    required_fields = {
        "id": int,
        "name": str,
        "price": (float, int),
        "stock": int,
        "product_category": str,
    }

    for field, field_type in required_fields.items():
        if field not in item_info:
            raise KeyError("{} field is not defined!".format(field))
        elif not isinstance(item_info[field], field_type):
            raise TypeError("Invalid type for field: {}".format(field))

    return True


def is_valid_customer(customer_info):
    required_fields = {
        "name": str,
        "surname": str,
        "email": str,
        "address": str,
    }

    for field, field_type in required_fields.items():
        if field not in customer_info:
            raise KeyError("{} field is not defined!".format(field))
        elif not isinstance(customer_info[field], field_type):
            raise TypeError("Invalid type for field: {}".format(field))

    return True


def print_store_matrix(matrix):
    column_widths = [
        max(len(str(item)) for item in column) + 2 for column in zip(*matrix)
    ]
    print("\n")
    total_width = sum(column_widths) + len(column_widths) - 1
    border_width = (total_width - len(" STORE ")) // 2
    print("+" + "-" * border_width + " STORE " + "-" * border_width + "+")

    header = "|".join(
        "{:^{width}}".format(column, width=width)
        for column, width in zip(matrix[0], column_widths)
    )
    print(header)

    separator = "+".join("-" * width for width in column_widths)
    print(separator)

    for row in matrix[1:]:
        row_str = "|".join(
            "{:^{width}}".format(str(item), width=width)
            for item, width in zip(row, column_widths)
        )
        print(row_str)

    print("+" + "-" * total_width + "+")
    print("\n")


def create_items_matrix(store):
    matrix = [["Item", "Stock", "Price", "Category", "Id"]]

    for item in store.items.values():
        matrix.append(
            [item.name, item.stock, item.price, item.product_category, item.id]
        )
    return matrix
