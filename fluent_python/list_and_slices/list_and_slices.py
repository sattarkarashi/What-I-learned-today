"""
Be aware of the lists mutable nature. We will explore a scenario for creating list of lists one of which
is the wrong and notmally misunderstood one.
"""
# The below code actually creates 3 references to the same list and assigning a value to one of the lists
# will change all the lists.

list_of_list = 3* [[]]

list_of_list[0].append(1)
print(list_of_list)

# The correct way to create a list of lists is to use a list comprehension as shown below:
list_of_list = [ [] for _ in range(3)]
list_of_list[0].append(1)
print(list_of_list)


# += operator uses __iadd__ method which is inplace and will change the original 
# list but + operator will create a new list

a = [1, 2, 3]
print(id(a))
b = [3,2]
a += b
print(id(a))

# if the __iadd__ method is not implemented in the class then the __add__ method will be used which
# will create a new list

a = [1, 2, 3]
print(id(a))
b = [3,2]
a = a + b
print(id(a))

# The below code will raise an error because the tuple is immutable and the += operator will try to change
# the tuple which is not possible and in fact it will change the tupel although it hits an error! So putting
# mutable objects in a tuple is not a good idea.
try:
    t = (1, 2, [30, 40])
    print(id(t))
    t[2] += [50, 60]
except Exception as e:
    print(e)

print(t)
print(id(t))