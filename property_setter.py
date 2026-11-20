class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

product = Product(10)
print(product.price)  # Output: 10

product.price = 20
print(product.price)  # Output: 20

   