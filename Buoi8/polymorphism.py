class MotorbikeDelivery:
    def calculate_fee(self, distance_km):
        fee = distance_km * 5000
        return fee


class GrabDelivery:
    def calculate_fee(self, distance_km):
        fee = distance_km * 7000
        return fee


class TruckDelivery:
    def calculate_fee(self, distance_km):
        fee = distance_km * 20000
        return fee


def get_shipping_cost(delivery_method, distance):
    return delivery_method.calculate_fee(distance)


print(get_shipping_cost(TruckDelivery(), 2))
