"""
Quiz 4.3
A palindrome is a word or a phrase that has the same characters
forwards and backwards. For example, "never odd or even", "racecar"
are palindromes.

Given a string containing a word or sequence of words, write a function
that determines if the string is a palindrome. You can assume that there
is no punctuation and all characters are lowercase.

Use a stack to determine palindromicity.
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
            new_list = Stack(self.capacity * 2)
            for i in range(self.actual):
                new_list.data[i] = self.data[i]
            new_list.data[self.top + 1] = item
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


# Use a stack to determine if it is a palindrone
def pal_check(phrase):
    characters = phrase.replace(" ", "").lower()
    new_stack = Stack()
    for x in characters:
        new_stack.push(x)
    for character in characters:
        if character != new_stack.pop():
            return False
    return True


print('Is "Dianna" a palindrone?')
print(pal_check("Dianna"))

print('\nIs "Never odd or even" a palindrone?')
print(pal_check("Never odd or even"))

print('\nIs "racecar" a palindrone?')
print(pal_check("racecar"))
