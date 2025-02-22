from collections import namedtuple
import time
from functools import singledispatch
from decimal import Decimal
from datetime import datetime
# Decorators

def deco_sample(func):
    def inner():
        print("Running inner")
    print("Decorator running")
    return inner

@deco_sample
def target_sample():
    print("Target sample running")

target_sample()

deco_sample(target_sample)()


# Refactoring the strategy pattern using a decorator whichs adds new promotions
Customer = namedtuple('Customer','name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:# the Context
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self,'__total'):
            self.__total= sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount=0
        else:
            discount = self.promotion(self)

        return self.total()-discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(),self.due())


promos = []  # The promotion registry

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity_promo(order):
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item_promo(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order_promo(order):
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

def best_promo(order):
    """Select best discount available"""
    return max(promo(order) for promo in promos)

sato = Customer("Sato", 2300)
sati = Customer("Sati", 800)

sato_cart = [
    LineItem('banana', 4, .5),
    LineItem('apple', 10, 1.5),
    LineItem('watermelon', 5, 5.0),
]

sati_cart = [
    LineItem('banana', 30, .5),
    LineItem('apple', 10, 1.5),
]
# Example usage with function-based strategy
order_sato_func = Order(sato, sato_cart, fidelity_promo)
print(f"Sato fidelity promo (function): {order_sato_func}")

order_sati_bulk_func = Order(sati, sati_cart, bulk_item_promo)
print(f"Sati bulk promo (function): {order_sati_bulk_func}")


@singledispatch
def formatted_output(arg):
    return f"Default format: {arg}"

@formatted_output.register
def _(arg: int):
    return f"Integer: {arg:+d}"

@formatted_output.register
def _(arg: float):
    return f"Float: {arg:.2f}"

@formatted_output.register
def _(arg: Decimal):
    return f"Decimal: {arg:.2f}"

@formatted_output.register
def _(arg: datetime):
    return f"Date/Time: {arg:%Y-%m-%d %H:%M:%S}"

# Test the single dispatch
print(formatted_output('Hello'))  # Default format
print(formatted_output(42))       # Integer format
print(formatted_output(3.14159))  # Float format
print(formatted_output(Decimal('3.14159')))  # Decimal format
print(formatted_output(datetime.now()))  # DateTime format



registery = set()

def register(active=True):
    def decorate(func):
        print("Running register (active = %s)-decorate(%s)"%(active, func))

        if active:
            registery.add(func)
        else:
            registery.discard(func)
        
        return func
    
    return decorate


@register(active=False)
def f1():
    print("Running f1")

@register()
def f2():
    print("Running f2")

def f3():
    print("Running f3")

print(registery)

register()(f3)
print(registery)




