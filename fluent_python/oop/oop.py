import copy

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.data = [1, 2, 3]

def create_cycle():
    # Create cycling reference
    node1 = Node("Node 1")
    node2 = Node("Node 2")
    node3 = Node("Node 3")

    # Create cycle
    node1.next = node2
    node2.next = node3
    node3.next = node1

    return node1

def copy_examples():
    # Original object
    original = Node("Original")
    
    # Shallow copy
    shallow = copy.copy(original)
    print("Shallow copy - same data list:", original.data is shallow.data)  # True
    
    # Deep copy
    deep = copy.deepcopy(original)
    print("Deep copy - same data list:", original.data is deep.data)  # False

    # Modify original data to show difference
    original.data.append(4)
    print("\nAfter modification:")
    print("Original data:", original.data)
    print("Shallow copy data:", shallow.data)  # Will show [1, 2, 3, 4]
    print("Deep copy data:", deep.data)  # Will show [1, 2, 3]

# if __name__ == "__main__":
# Demonstrate cycle
cycle = create_cycle()
print("Cycling reference example:")
print(f"cycle.next.next.next is cycle: {cycle.next.next.next is cycle}")

# Demonstrate copying
print("\nCopy examples:")
copy_examples()

# Example of mutable default value problem
class BadList:
    def __init__(self, items=[]):  # Mutable default - BAD!
        self.items = items
    
    def add_item(self, item):
        self.items.append(item)

class GoodList:
    def __init__(self, items=None):  # Immutable default - GOOD!
        self.items = items if items is not None else []
    
    def add_item(self, item):
        self.items.append(item)

# Demonstrate the problem
print("\nMutable default value problem:")
list1 = BadList()
list2 = BadList()
list1.add_item('a')
print("list1:", list1.items)
print("list2:", list2.items)  # Unexpectedly contains 'a'!
print(BadList.__init__.__defaults__)

# Show correct implementation
good1 = GoodList()
good2 = GoodList()
good1.add_item('a')
print("\nCorrect implementation:")
print("good1:", good1.items)
print("good2:", good2.items)  # Correctly empty