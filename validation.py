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
