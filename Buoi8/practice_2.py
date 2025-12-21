class BankAccount:
    def __init__(self, owner, __balance):
        self.owner = owner
        self.__balance = __balance

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        return f"Tiền sau khi tăng: {self.__balance}"

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance = self.__balance - amount
            return f"Tiền sau khi trừ: {self.__balance}"
        else:
            return f"Không đủ tiền"

    def get_balance(self):
        return self.__balance


account_obj = BankAccount("Phú", 10)
print(account_obj.deposit(33))
print(account_obj.withdraw(93))
print(account_obj.get_balance())
