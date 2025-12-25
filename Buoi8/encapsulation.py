class Phone:
    def __init__(self):
        self.__battery_level = 100

    def use_app(self, hours):
        for i in range(1, hours + 1):
            if self.__battery_level > 0:
                self.__battery_level -= 10
            else:
                self.__battery_level = 0
                break

    def charge_phone(self, hours):
        for i in range(1, hours + 1):
            if self.__battery_level < 100:
                self.__battery_level += 20
            else:
                self.__battery_level = 100
                break

    def display_battery(self):
        return self.__battery_level


obj = Phone()

obj.use_app(9)
obj.charge_phone(3)
print(obj.display_battery())
