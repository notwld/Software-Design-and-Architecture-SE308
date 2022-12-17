# composite design pattern example

class PC:
    def __init__(self, name):
        self.name = name
        self.parts = []
    def add(self, part):
        self.parts.append(part)
    def remove(self, part):
        self.parts.remove(part)
    def get_price(self):
        price = 0
        for part in self.parts:
            price += part.get_price()
        return price
    def get_name(self):
        return self.name

class Part:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_price(self):
        return self.price
    def get_name(self):
        return self.name

if __name__ == '__main__':
    pc = PC('PC')
    cpu = Part('CPU', 100)
    ram = Part('RAM', 50)
    pc.add(cpu)
    pc.add(ram)
    print('Total price of {} is {}'.format(pc.get_name(), pc.get_price()))