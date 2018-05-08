"""
Part 1 — Dynamic Arrays
Using your language’s existing array structure, implement a dynamic array-based list.
Python users: since Python doesn’t have the kind of array we want,
copy/use this link for your array type.
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
        # If array is empty, create a new array with size 1
        if self.capacity == 0:
            new_list = DynamicArray(1)
            new_list.data[0] = value
            self.data = new_list.data
            self.capacity = 1
            self.actual = 1

        elif self.actual + 1 <= self.capacity:
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


# Test - create an empty array
x = DynamicArray()
print("Array contains: {}".format(x))
print("Type: {}\n".format(type(x)))

# Test - append value at end of list
print('Add "one" to the end of the array.')
x.append("one")
print("Array contains: {}\n".format(x))

print('Add "two" to the end of the array.')
x.append("two")
print("Array contains: {}\n".format(x))

print('Add "three" to the end of the array.')
x.append("three")
print("Array contains: {}\n".format(x))

# Test - set value at specific index
x.set(0, "zero")
print('Set item at index 0 to "zero".')
print("Array contains: {}".format(x))

# Test - get value at a specific index
print("\nValue at index 1 is: {}\n".format(x.get(1)))

# Test - search for a value
print('Is "one" in the array?')
print(x.search("one"))
print('Is "two" in the array?')
print(x.search("two"))

# Test - length of array
print("\nLength of array is: {}\n".format(len(x)))
