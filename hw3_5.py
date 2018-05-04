"""
Homework 3.5
Implement a queue using a linked list.
Feel free to use your linked list implementation from homework 2.
Your queue should start empty and support the following methods:
•	enqueue(item) adds the item to the back of the queue
•	dequeue() removes and returns the item at the front of the queue
•	peek() returns the front-most item, but does not remove it
•	isEmpty() returns true if the queue is empty
•	size() returns the number of items in the queue
"""


# Create a node
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        if self.next is None:
            return self.data
        else:
            return self.data + str(self.next)


# Create a Queue using a Linked List
class Queue:
    def __init__(self):
        self.head = None

    # Enqueue - add a value to the end of the list
    def enqueue(self, new_node):
        current_index = 0
        current_node = self.head

        if current_node is None:
            self.head = Node(new_node)
        else:
            while current_node.next is not None:
                current_index += 1
                current_node = current_node.next
            current_node.next = Node(new_node)

    # Dequeue - remove value at the beginning of the list
    def dequeue(self):
        current_node = self.head
        if current_node is None:
            return "Queue is empty."
        else:
            self.head = current_node.next
        return self.head

        # Peek - return the item at the front, but do not remove it

    def peek(self):
        current_node = self.head
        return current_node.data

    # Empty - Check if the queue is Empty
    def is_empty(self):
        current_node = self.head
        if current_node is None:
            return True
        else:
            return False

    # Size - Count the number of items in the queue
    def size(self):
        counter = 0
        current_node = self.head
        if current_node is None:
            return 0
        else:
            while current_node is not None:
                counter += 1
                current_node = current_node.next
        return counter

    # Format list as a string
    def __str__(self):
        current_node = self.head
        qstring = ""
        if current_node is None:
            return "Empty"
        else:
            while current_node is not None:
                qstring += str(current_node.data)
                qstring += "-->"
                current_node = current_node.next
        qstring += "End"
        return qstring


# Test - create a queue
print("Create a queue.")
q = Queue()
print("Queue contains: {}".format(q))

print('\nAdd "A" to the queue.')
q.enqueue("A")
print("Queue contains: {}".format(q))

print('\nAdd "B" to the queue.')
q.enqueue("B")
print("Queue contains: {}".format(q))

print('\nAdd "C" to the queue.')
q.enqueue("C")
print("Queue contains: {}".format(q))

print("\nRemove item from the front of the queue.")
q.dequeue()
print("Queue contains: {}".format(q))

print("\nPeek at the item at the front of the queue.")
print(q.peek())
print("Queue contains: {}".format(q))

print("\nWhat is the size of the queue?")
print(q.size())

print("\nIs the queue empty?")
print(q.is_empty())
