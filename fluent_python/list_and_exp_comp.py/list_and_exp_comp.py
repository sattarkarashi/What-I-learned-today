"""
List comprehensions can do cartesian products
"""

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

tshirts = [(color, size) for size in sizes for color in colors]
print(tshirts)

# These type of list comprehensions work like nested loops indeed.abs

# Genexp or generator expressions
a = (x for x in range(10))
print(list(a))
