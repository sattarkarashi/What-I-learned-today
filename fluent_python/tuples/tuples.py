"""
Definging tuples as immutable lists is shortselling them. In tuples, the order of elements is important, but the elements themselves are not.
 Tuples are used to group together related data, such as a person's name, their age, and their other information.
"""

# Ways of unpacking tuples
a, b, c = (1, 2, 3)
print(a,b,c)

# Swapping values
t = (18, 4)
quotient, remainder = divmod(*t)
print(quotient, remainder)

a, b, *rest = range(5)
print(a, b, rest)

a, *body, c, d = range(5)
print(a, body, c, d)

# Pattern matching in nested tuples
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))

for name, cc, pop, (lat, long) in metro_areas:
    if long <= 0:
        print('{:15} | {:9.4f} | {:9.4f}'.format(name, lat, long))
    

# Named tuples
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)

# Named tuples take as much memory as regular tuples as they do not have per-instance dictionaries.