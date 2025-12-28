from abc import ABC, abstractmethod


class PaymentGetway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class MomoPayment(PaymentGetway):
    def process_payment(self, amount):
        return f"Đang xử lý thanh toán Momo số tiền {amount}, Vui lòng quét mã QR."


class CreditCaraPayment(PaymentGetway):
    def process_payment(self, amount):
        return (
            f"Đang xử lý thanh toán Momo số tiền {amount}, Vui lòng nhập thông tin thẻ."
        )


obj = MomoPayment()
print(obj.process_payment(20))

obj = CreditCaraPayment()
print(obj.process_payment(20))
