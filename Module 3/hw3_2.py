"""
Homework 3.2 - Implement a stack
Feel free to use your dynamic array implementation from homework 2
Your stack should start empty and support the following methods:
•	push(item) adds the item to the top of the stack
•	pop() removes and returns the most recently added item
•	peek() returns the most recently added item, but does not remove it
•	isEmpty() returns true if the stack is empty
•	size() returns the number of items on the stack
"""


# Create a Stack using a Dynamic Array
class Stack:

    def __init__(self, size=0):

        # Data
        self.data = [None] * size

        # Actual size
        self.actual = 0

        # Total capacity
        self.capacity = size

        # Set top of stack
        self.top = -1

    # Convert data to string format
    def __str__(self):
        return str(self.data)

    # Add a value to the top of the stack
    def push(self, item):

        # If stack is empty, create a new stack with size 1
        if self.capacity == 0:
            new_list = Stack(1)
            new_list.data[0] = item
            self.data = new_list.data
            self.capacity = 1
            self.actual = 1
            self.top = 0

        # If not enough room, create a new array and copy items
        elif self.top + 1 == self.capacity:
            new_list = Stack(self.capacity*2)
            for i in range(self.actual):
                new_list.data[i] = self.data[i]
            new_list.data[self.top+1] = item
            self.capacity *= 2
            self.actual += 1
            self.data = new_list.data
            self.top += 1
        # Otherwise just add the new item
        else:
            self.data[self.top + 1] = item
            self.top += 1
            self.actual += 1

    # Remove value from top of the Stack
    def pop(self):
        if self.top >= 0:
            pop_value = self.data[self.top]
            self.data[self.top] = None
            self.top -= 1
            self.actual -= 1
            return pop_value
        else:
            return "Stack is empty."

    # Return most recently added item but do not remove item
    def peek(self):
        if self.top >= 0:
            return self.data[self.top]
        else:
            return "Stack is empty."

    # Check the length of the stack
    def size(self):
        return self.actual

    # Check if stack is empty
    def is_empty(self):
        if self.top < 0:
            return True
        else:
            return False


# Test - create a Stack
print("Create a stack.")
s = Stack()
print("Stack contains: {}".format(s))

# Test - push an item
print('\nPush the item "one".')
s.push("one")
print("Stack contains: {}".format(s))

print('Push the item "two".')
s.push("two")
print("Stack contains: {}".format(s))

print('Push the item "three".')
s.push("three")
print("Stack contains: {}".format(s))

print("\nPop the last value.")
print(s.pop())
print("Stack contains: {}".format(s))

print("\nPeek at the last value.")
print(s.peek())
print("Stack contains: {}".format(s))

print("\nWhat is the size of the stack?")
print(s.size())

print("\nIs the stack empty?")
print(s.is_empty())
