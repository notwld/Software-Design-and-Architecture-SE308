from abc import ABC, abstractmethod
class Order(ABC):
    @abstractmethod 
    def process(self):
        pass

class BuyStock(Order): 
    def __init__(self, stock):
        self.stock = stock 
    def process(self):         
        self.stock.buy()

class SellStock(Order):
    def __init__(self, stock):
        self.stock = stock 
    def process(self):         
        self.stock.sell()

class Trade: 
    def buy(self):
        print("Stock buy request placed.")
    def sell(self): 
        print("Stock sell request placed.") 
class Invoker:     
    def __init__(self):         
        self._queue = [] 
    def process_order(self, order):         
        self._queue.append(order)         
        order.process() 
 
trade = Trade() 
buy_stock = BuyStock(trade) 
sell_stock = SellStock(trade) 
 
invoker = Invoker() 
invoker.process_order(buy_stock) 
invoker.process_order(sell_stock)  
