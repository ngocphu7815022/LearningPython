class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Không thể chia cho 0"
        else:
            return a / b


calculator_obj = Calculator()
print(calculator_obj.add(10, 0))
print(calculator_obj.subtract(10, 0))
print(calculator_obj.multiply(10, 0))
print(calculator_obj.divide(10, 0))
