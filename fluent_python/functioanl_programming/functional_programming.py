# Although it is almost impossible to use python as a functional porgramming language but it is a good
# practice to use a functional programming style. 

from functools import reduce

def fact(n):
    return reduce(lambda a,b:a*b, range(1, n+1))

print(fact(5))

from operator import mul
from operator import itemgetter

def fact(n):
    return reduce(mul, range(1, n+1))

print(fact(5))

# Example with a list of tuples
inventory = [('apple', 3), ('banana', 2), ('orange', 5)]
get_quantity = itemgetter(1)
print(sorted(inventory, key=get_quantity))  # sorts by quantity

# Example with dictionaries
products = [{'name': 'apple', 'price': 0.5}, {'name': 'banana', 'price': 0.3}]
get_price = itemgetter('price')
print(sorted(products, key=get_price))  # sorts by price