init -5 python:
    class Inventory(store.object):
        def __init__(self, money=10, space=30):
            self.money = money
            self.items = []
            self.space = space
        def add(self, item): # a simple method that adds an item; we could also add conditions here (like check if there is space in the inventory)
            if self.space > 0:
                self.items.append(item)
                self.space -= item.space
        def drop(self, item):
            self.items.remove(item)
            self.space += item.space
        def buy(self, item):
            if self.money >= item.cost:
                self.items.append(item)
                self.money -= item.cost
                self.space -= item.space
        def sell(self, item):
            self.items.remove(item)
            self.money += item.cost *0.9
            self.space += item.space
