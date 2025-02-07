# User defined callable types
import random

class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndentationError:
            raise LookupError("Pick from empty BingoCage")
    
    def __call__(self):
        return self.pick()


bingo = BingoCage(range(5))

print(bingo())
print(callable(bingo))

# Attributes of functions that don't exist in plain isntances

class C:
    pass
obj = C()

def func():
    pass


print(sorted(set(dir(func))-set(dir(obj))))


