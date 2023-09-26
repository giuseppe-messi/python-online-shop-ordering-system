class Item:
    def __init__(self, item_info):
        self.id = item_info.get("id")
        self.name = item_info.get("name")
        self.price = item_info.get("price")
        self.product_category = item_info.get("product_category")
