from OCInterface import Order as IOrder, Payment


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
    @staticmethod
    def pay(order: Order, code: int):
        print(f'Payment is processing using debit card.')
        print(f'Validating code {code}.')
        order.status = 'Paid'
        print(f'Payment Successful')


class CreditPayment(Payment):
    @staticmethod
    def pay(order: Order, code: int):
        print(f'Payment is processing using credit card.')
        print(f'Validating code {code}.')
        order.status = 'Paid'
        print(f'Payment Successful')


# Testing.
order = Order()
order.add_items("Bajwa", 100, 2)
order.add_items("Waleed", 500, 2)
order.calculate_total()

# Pay debit.
debit_payment = DebitPayment()
debit_payment.pay(order, 123)

# Pay credit.
credit_payment = CreditPayment()
credit_payment.pay(order, 123)
