"""
Part 1 — Dynamic Arrays
Using your language’s existing array structure, implement a dynamic array-based list.
Python users: since Python doesn’t have the kind of array we want, copy/use this link for your array type.
Submit file as HW2_1_Dianna_Tingg.py
"""

# Create a Dyanmic Array Class
class DynamicArray:
    def __init__(self, size=0):
        self.data = [None] * size

        # Actual size
        self.actual = size

        # Total capacity
        self.capacity = size

    # Convert data to string format
    def __str__(self):
        return str(self.data)

    # Check index number to see if it is in range
    def _key_to_index(self, key):
        try:
            index = int(key)
            if index >= self.actual or index < 0:
                raise IndexError("Array index out of range")
            else:
                return index
        except ValueError:
            raise TypeError("Array indices must be integers")

    # Set value at specific index
    def set(self, key, value):
        try:
            index = self._key_to_index(key)
            self.data[index] = value

        except IndexError:
            print("Error. Index out of range.")
        except TypeError:
            print("Error. Index must be an integer.")

    # Get value at a specific index location
    def get(self, key):
        try:
            index = self._key_to_index(key)
            return self.data[index]
        except IndexError:
            print("Error. Index out of range.")
        except TypeError:
            print("Error. Index must be an integer.")

    # Append value to the end of the list
    def append(self, value):
        if self.actual + 1 <= self.capacity:
            self.set(self.actual, value)
            self.actual += 1
            return self.data

        else:
            new_list = DynamicArray(self.capacity * 2)
            for i in range(self.actual):
                new_list.set(i, self.data[i])
            new_list.set(self.actual, value)
            self.capacity *= 2
            self.actual += 1
            self.data = new_list.data
            return self.data

    # Search for a value
    def search(self, value):
        for i in range(self.actual):
            if self.data[i] == value:
                return True
        return False

    # Find length of array
    def __len__(self):
        length = self.actual
        return length

# Test - create an array
x = DynamicArray(3)
print("Array contains: {}".format(x))
print("Type: {}\n".format(type(x)))

# Test - set value at specific index
x.set(0, "one")
x.set(1, "two")
x.set(2, "three")
print('Set index 0 to "one", index 1 to "two", and index 2 to "three".')
print("Array contains: {}\n".format(x))

# Test - try to set value outside of index
print('Try to set index 3 to "test".')
x.set(3, "test")

# Test - try to use a non-integer index
print('\nTry to set index a to "try".')
x.set("a", "try")

# Test - get value at a specific index
print("\nValue at index 1 is: {}".format(x.get(1)))
print("Value at index 4 is:")
x.get(4)
print("Value at index z is:")
x.get("z")

# Test - append value at end of list
print('\nAdd "four" to the end of the array.')
print("Array contains: {}\n".format(x.append("four")))

# Test - search for a value
print('Is "one" in the array?')
print(x.search("one"))
print('Is "five" in the array?')
print(x.search("five"))
print('Is "None" in the array?')
print(x.search("None"))

# Test - length of array
print("\nLength of array is: {}".format(len(x)))
