class ShoppingCart:
    def __init__(self):
        self.items = []  # empty list for each new cart

    def add_item(self, item):
        self.items.append(item)

cart1 = ShoppingCart()
cart1.add_item("Apples")
cart1.add_item("Graphes")
cart1.add_item("Oranges")

cart2 = ShoppingCart()
cart2.add_item("Oranges")
cart2.add_item("Apples")
cart2.add_item("Banana")

print(cart1.items)
print(cart2.items)
