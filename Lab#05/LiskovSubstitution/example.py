from LSInterface import Order as IOrder, Payment


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


class DebitPayment(Payment):
    def __init__(self, code: int):
        self.code = code

    def pay(self, order: Order):
        print(f'Payment is processing using debit card.')
        print(f'Validating code {self.code}.')
        order.status = 'Paid'
        print(f'Payment Successful')


class CreditPayment(Payment):
    def __init__(self, code: int):
        self.code = code

    def pay(self, order: Order):
        print(f'Payment is processing using credit card.')
        print(f'Validating code {self.code}.')
        order.status = 'Paid'
        print(f'Payment Successful')


class VisaPayment(Payment):
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
