class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def devide(sel, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Không thể chia cho 0"


new_obj = Calculator()
print(new_obj.add(10, 0))
print(new_obj.subtract(10, 0))
print(new_obj.multiply(10, 0))
print(new_obj.devide(10, 0))
