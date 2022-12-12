from DIInterface import Order as IOrder, ExamplePayment
from abc import abstractmethod, ABCMeta


class Authorize:
    is_valid = False

    def verify(self) -> None:
        self.is_valid = True

    def is_authorized(self) -> bool:
        return self.is_valid


class GenericAuthentication(metaclass=ABCMeta):
    @abstractmethod
    def is_authorized(self) -> bool:
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


class DebitPayment(ExamplePayment):

    def __init__(self, code: int, validator: GenericAuthentication):
        self.code = code
        self.validator = validator

    def pay(self, order: Order):
        if not self.validator.is_authorized():
            raise Exception("User not verified.")
        print(f'Payment is processing using debit card.')
        print(f'Validating code {self.code}.')
        order.status = 'Paid'
        print(f'Payment Successful')


class CreditPayment(ExamplePayment):

    def __init__(self, code: int, validator: GenericAuthentication):
        self.code = code
        self.validator = validator

    def pay(self, order: Order):
        if not self.validator.is_authorized():
            raise Exception("User not verified.")
        print(f'Payment is processing using credit card.')
        print(f'Validating code {self.code}.')
        order.status = 'Paid'
        print(f'Payment Successful')


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

# validate
validator = Authorize()

# Payment.
visa_payment = CreditPayment(123, validator)
validator.verify()
visa_payment.pay(order)
