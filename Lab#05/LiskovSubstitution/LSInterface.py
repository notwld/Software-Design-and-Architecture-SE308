from abc import ABCMeta, abstractmethod


class Order(metaclass=ABCMeta):
    @abstractmethod
    def add_items(self, item_name: str, price: float, quantity: int) -> None:
        pass

    @abstractmethod
    def calculate_total(self) -> None:
        pass


class DemoPayment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, order: Order, code: int) -> None:
        pass


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, order: Order) -> None:
        pass
