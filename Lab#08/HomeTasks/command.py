from abc import ABC, abstractmethod

class Food:
    @abstractmethod
    def cook(self):
        pass

class Pizza(Food):
    def cook(self):
        print('Pizza is cooking')

class Burger(Food):
    def cook(self):
        print('Burger is cooking')

class FoodCommand:
    def __init__(self, food):
        self.food = food

    def execute(self):
        self.food.cook()

class Waiter:
    def __init__(self):
        self.__commands = []

    def add_command(self, command):
        self.__commands.append(command)

    def remove_command(self, command):
        self.__commands.remove(command)

    def execute_commands(self):
        for command in self.__commands:
            command.execute()

if __name__ == '__main__':
    pizza = Pizza()
    burger = Burger()

    pizza_command = FoodCommand(pizza)
    burger_command = FoodCommand(burger)

    waiter = Waiter()
    waiter.add_command(pizza_command)
    waiter.add_command(burger_command)

    waiter.execute_commands()

