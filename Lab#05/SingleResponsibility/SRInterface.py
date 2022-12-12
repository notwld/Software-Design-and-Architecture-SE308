from abc import ABCMeta, abstractmethod


class Order(metaclass=ABCMeta):
    @abstractmethod
    def add_items(self, item_name: str, price: float, quantity: int) -> None:
        pass

    @abstractmethod
    def calculate_total(self) -> None:
        pass


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def debit(self, order: Order) -> None:
        pass

    @abstractmethod
    def credit(self, order: Order) -> None:
        pass


class DemoOrder(metaclass=ABCMeta):
    @abstractmethod
    def add_items(self, item_name: str, price: float, quantity: int) -> None:
        pass

    @abstractmethod
    def calculate_total(self) -> None:
        pass

    @abstractmethod
    def payment(self, payment_type: str, code: int) -> None:
        pass
