class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

product = Product(10)
print(product.price)  # Output: 10

product.price = -20
print(product.price)  # Output: 20 """

object = Product(-50)
print(object.price)  # Output: 50

class Rect:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    @area.setter
    def area(self, value):
        raise AttributeError("Area is a read-only property and cannot be set directly.")

r = Rect(4, 5)
print(r.area)  # Output: 20
   