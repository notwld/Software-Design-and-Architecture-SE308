from abc import abstractmethod
from ISInterface import Order as IOrder, DemoPayment, ExamplePayment


class PaymentWithAuth(DemoPayment):

    @abstractmethod
    def two_factor_auth(self) -> None:
        pass


class Order(IOrder):
    items = []
    status = "Not Paid"

    def add_items(self, item_name: str, price: float, quantity: int):
        item = {
            "name": item_name,
            "price": price,
            "quantity": quantity
        }

        self.items.append(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.get('price') * item.get('quantity')

        return total


class DebitPayment(PaymentWithAuth):

    def __init__(self, code: int):
        self.is_verified = False
        self.code = code

    def pay(self, order: Order):
        if not self.is_verified:
            raise Exception("User not verified.")
        print(f'Payment is processing using debit card.')
        print(f'Validating code {self.code}.')
        order.status = 'Paid'
        print(f'Payment Successful')

    def two_factor_auth(self):
        self.is_verified = True


class CreditPayment(PaymentWithAuth):
    def __init__(self, code: int):
        self.code = code
        self.is_verified = False

    def pay(self, order: Order):
        if not self.is_verified:
            raise Exception("User not verified.")
        print(f'Payment is processing using credit card.')
        print(f'Validating code {self.code}.')
        order.status = 'Paid'
        print(f'Payment Successful')

    def two_factor_auth(self):
        self.is_verified = True


class VisaPayment(ExamplePayment):
    def __init__(self, email: str):
        self.email = email

    def pay(self, order: Order):
        print(f'Payment is processing using credit card.')
        print(f'Validating code {self.email}.')
        order.status = 'Paid'
        print(f'Payment Successful')


# Testing.
order = Order()
order.add_items("Bajwa", 100, 2)
order.add_items("Waleed", 500, 2)
order.calculate_total()

# Payment.
visa_payment = VisaPayment('test@gmail.com')
visa_payment.pay(order)
