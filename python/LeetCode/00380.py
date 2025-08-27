import random

class RandomizedSet:

    def __init__(self):
        self.items = set()
        self.values = []

    def insert(self, val: int) -> bool:
        l1 = len(self.items)
        self.items.add(val)
        if l1 == len(self.items):
            return False
        else:
            self.values.append(val)
            return True

    def remove(self, val: int) -> bool:
        l1 = len(self.items)
        self.items.discard(val)
        if l1 == len(self.items):
            return False
        else:
            self.values.remove(val)
            return True

    def getRandom(self) -> int:
        return random.choice(self.values)