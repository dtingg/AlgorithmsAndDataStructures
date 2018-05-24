"""
Quiz 7
Question 4
Implement a Set using a dictionary
"""


class Set:
    def __init__(self):
        self.d = {}

    # Add item to the set
    def add(self, item):
        self.d[item] = True

    # Remove item from the set
    def remove(self, item):
        del self.d[item]

    # Check if the item already exists in the set
    def contains(self, item):
        return item in self.d

    def __iter__(self):
        return iter(self.d)

    def __str__(self):
        return str(self.d.keys())


fruits = Set()
fruits.add("mango")
fruits.add("peach")
print(fruits.contains("mango"))
