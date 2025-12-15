class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car_object1 = Car("Toyota", "Camry")
car_object2 = Car("Vinfast", "VF8")

print(car_object1.brand, car_object1.model)
print(car_object2.brand, car_object2.model)
