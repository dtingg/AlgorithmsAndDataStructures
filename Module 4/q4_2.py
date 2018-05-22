"""
Quiz 4.2

Implement a queue using two stacks.
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


# Implement a queue using two stacks
class TwoStackQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        while self.stack2.actual != 0:
            transfer = self.stack2.pop()
            self.stack1.push(transfer)
        self.stack1.push(item)

    def dequeue(self):
        while self.stack1.actual != 0:
            transfer = self.stack1.pop()
            self.stack2.push(transfer)
        return self.stack2.pop()

    def peek(self):
        while self.stack1.actual != 0:
            transfer = self.stack1.pop()
            self.stack2.push(transfer)
        return self.stack2.peek()


# Test queue using two stacks
print("Create a queue using two stacks.")
q = TwoStackQueue()

print("Add A, B, and C to the queue.")
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

print("\nRemove item from the queue.")
print(q.dequeue())

print("\nAdd D, E, F to the queue.")
q.enqueue("D")
q.enqueue("E")
q.enqueue("F")

print("\nRemove item from the queue.")
print(q.dequeue())

print("\nPeek at next item in the queue.")
print(q.peek())

print("\nRemove item from the queue.")
print(q.dequeue())
