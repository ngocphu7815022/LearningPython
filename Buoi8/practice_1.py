class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2


rec_obj = Rectangle(3, 4)
print(rec_obj.get_area())
print(rec_obj.get_perimeter())
