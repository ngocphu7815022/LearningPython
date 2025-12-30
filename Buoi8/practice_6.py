class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Giá không thể âm")
        else:
            self._price = value

    def get_total_price(self, quantity):
        return self._price * quantity


obj = Product(10)
print(obj.price)  # price = 10
obj.price = 4
print(obj.price)  # Error
print(obj.get_total_price(2))  # price = 10 * 2 = 20
