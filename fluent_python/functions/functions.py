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

def tag(name, *content, cls=None, **attrs):
    '''
    Generate one or more tags
    '''
    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attr_str = "".join('%s= "%s"'%(attr, value) for atr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    
    if content:
        return '\n'.join("<%s%s>%s<%s>"%(name, attr_str, c, name) for c in content)
    else:
        return "<%s%s />"%(name, attr_str)

print(tag('br'))
print(tag('p','hello'))

print(tag.__code__.co_argcount)
print(tag.__code__.co_varnames)
print(tag.__defaults__)

from inspect import signature

sig = signature(tag)
print(str(sig))

