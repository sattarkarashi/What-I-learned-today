from abc import ABC, abstractmethod
from collections import namedtuple

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
            discount = self.promotion.discount(self)

        return self.total()-discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(),self.due())


class Promotion(ABC):# the Strategy: an Abstract Base Class
    @abstractmethod
    def discount(self,order):
        """Return discount as a positive dollar amount"""
        pass


class FidelityPromo(Promotion):# first Concrete Strategy
    """5% discount for customers with 1000 or more fidelity points"""

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):# second Concrete Strategy
    """10% discount for each LineItem with 20 or more units"""

    def discount(self,order):
        discount=0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total()*.1
        return discount


class LargeOrderPromo(Promotion):# third Concrete Strategy
    """7% discount for orders with 10 or more distinct items"""

    def discount(self,order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items)>=10:
            return order.total()*.07
        return 0


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

# Create orders with different promotions
order_sato = Order(sato, sato_cart, FidelityPromo())
print(f"Sato fidelity promo: {order_sato}")

order_sati_bulk = Order(sati, sati_cart, BulkItemPromo())
print(f"Sati bulk promo: {order_sati_bulk}")

# Since our promo classes have only on method, we can turn them into functions and 
# use a funcion oriented strategy instead of class based one.


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

def fidelity_promo(order):
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

def large_order_promo(order):
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

# Example usage with function-based strategy
order_sato_func = Order(sato, sato_cart, fidelity_promo)
print(f"Sato fidelity promo (function): {order_sato_func}")

order_sati_bulk_func = Order(sati, sati_cart, bulk_item_promo)
print(f"Sati bulk promo (function): {order_sati_bulk_func}")