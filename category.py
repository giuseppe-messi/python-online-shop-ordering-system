class Category:
    def __init__(self, name: str):
        self.name = name
        self.items = {}

    def add_item(self, item):
        """
        Add an item to the category.
        """

        self.items[item.id] = item
