class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity

    def display_info(self):
        print(
            f"Product: {self.name}, Unit price: {self.price}, Quantity: {self.quantity}, Total price: {self.get_total_price()}"
        )


product_obj = Product("T-shirt", 10, 3)
product_obj.display_info()
