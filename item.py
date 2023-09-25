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
