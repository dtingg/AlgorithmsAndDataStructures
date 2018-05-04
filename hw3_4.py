"""
Homework 3.4
Use your stack implementation from problem 2 to implement problem 3.
You function can take an input of either the string of parentheses,
or a list of individual parentheses.
A common problem for compilers and text editors is determining whether
the parentheses in a string are balanced and properly nested.
For example, the string ((())())() contains properly nested pairs of
parentheses, which the strings )()( and ()) do not.
Create an algorithm that returns true if a string contains properly
nested and balanced parentheses, and false if otherwise.
Extra: Identify the position of the first offending parenthesis
if the string is not properly nested and balanced.
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

        # Create a balance for parens
        self.balance = True

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
            self.balance = False
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

    # Check if parens are balanced and properly nested
    def check_parens(self, values):
        length = len(values)
        new_stack = Stack(length)
        self.data = new_stack.data

        if values[0] == ")":
            print("Offender is at index 0.")
            return False

        for i in range(length):
            if values[i] == "(":
                self.push("open")
            elif values[i] == ")":
                self.pop()
                if self.balance is False:
                    print("Offender is at index {}.".format(i))
                    return False

        if self.is_empty() is True:
            return True
        else:
            print("Offender is at index {}.".format(length - 1))
            return False


# Test - check a string to see if the parens are balanced/nested
string1 = "((())())()"
print("String 1 is: {}".format(string1))
a = Stack()
print("Are the parens correct? {}".format(a.check_parens(string1)))

# Test - check a string to see if the parens are balanced/nested
string2 = ")()("
print("\nString 2 is: {}".format(string2))
b = Stack()
print("Are the parens correct? {}".format(b.check_parens(string2)))

# Test - check a string to see if the parens are balanced/nested
string3 = "())"
print("\nString 3 is: {}".format(string3))
c = Stack()
print("Are the parens correct? {}".format(c.check_parens(string3)))

# Test - check a list to see if the parens are balanced/nested
list1 = ["(", "(", "(", ")", ")", "(", ")", ")", "(", ")"]
print("\nList 1 is: {}".format(list1))
d = Stack()
print("Are the parens correct? {}".format(d.check_parens(list1)))

# Test - check a list to see if the parens are balanced/nested
list2 = [")", "(", ")", "("]
print("\nList 2 is: {}".format(list2))
e = Stack()
print("Are the parens correct? {}".format(e.check_parens(list2)))

# Test - check a list to see if the parens are balanced/nested
list3 = ["(", ")", ")"]
print("\nList 3 is: {}".format(list3))
f = Stack()
print("Are the parens balanced? {}".format(f.check_parens(list3)))
