class Pizza(object):
    def __init__(self):
        self._price = None

    def get_price(self): return self._price


class MexicanPizza(Pizza):
    def __init__(self):
        self._price = 8.5


class DeluxePizza(Pizza):
    def __init__(self):
        self._price = 10.5


class HawaiianPizza(Pizza):
    def __init__(self):
        self._price = 11.5


class PizzaFactory(object):
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == 'Mexican':
            return MexicanPizza()
        elif pizza_type == 'Deluxe':
            return DeluxePizza()
        elif pizza_type == 'Hawaiian':
            return HawaiianPizza()


if __name__ == '__main__':
    for pizza_type in ('Mexican', 'Deluxe', 'Hawaiian'):
        print('Price of {0} pizza is {1}'.format(pizza_type,
              PizzaFactory.create_pizza(pizza_type).get_price()))
