class Category:
    def __init__(self, name):
        self.name = name
        self.items = {}

    def add_item(self, item):
        self.items[item.id] = item
