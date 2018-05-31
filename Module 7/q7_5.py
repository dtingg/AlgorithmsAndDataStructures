"""
Quiz 7
Question 5
List overlap

Determine how much overlap two customers have in their viewing history.
Assuming that you've been provided with two lists containing all of the
shows two different customers have watched, write a function that returns
the list of shows that both customers have seen.
"""


# Class for set
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


# Function for list overlap
def overlap(first, second):
    s = Set()
    intersect = Set()

    for item in first:
        s.add(item)

    for item in second:
        if s.contains(item):
            intersect.add(item)
    return intersect


yogi = ["Breaking Bad", "Stargate SG-1", "Louie", "Black Mirror", "Stranger Things"]

amanda = ["Gilmore Girls", "Breaking Bad", "Stranger Things", "Dexter"]

print(overlap(yogi, amanda))
