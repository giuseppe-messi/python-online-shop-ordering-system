from order import Order
from type_definitions import CustomerInfoType
from utils import handle_operation_errors, is_valid_customer


class Customer:
    @handle_operation_errors
    def __init__(self, store, customer_info: CustomerInfoType):
        is_valid_customer(customer_info)

        self.store = store
        self.name = customer_info.get("name")
        self.surname = customer_info.get("surname")
        self.__email = customer_info.get("email")
        self.__address = customer_info.get("address")
        self.order = Order(self, store)
