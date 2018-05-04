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
    def __init__(self, start):
        self.head = Node(start)

    # Get value at a specific index
    def get(self, index):
        current_index = 0
        current_node = self.head

        try:
            while current_index != index:
                current_index += 1
                current_node = current_node.next
            return current_node.data

        except AttributeError:
            return print("Error. Index not in range.")

    # Search for some value
    def search(self, needle):
        current_node = self.head
        while current_node is not None:
            if current_node.data == needle:
                return True
            current_node = current_node.next
        return False

    # Change value at specific location
    def change(self, new_value, index):
        current_index = 0
        current_node = self.head

        try:
            while current_index != index:
                current_index += 1
                current_node = current_node.next
            current_node.data = new_value
            return self.head

        except AttributeError:
            return print("Error. Index not in range.")

    # Enqueue - add a value to the end of the list
    def enqueue(self, new_node):
        current_index = 0
        current_node = self.head
        while current_node.next is not None:
            current_index += 1
            current_node = current_node.next
        current_node.next = Node(new_node)
        return self.head

    # Dequeue - remove value at the beginning of the list
    def dequeue(self):
      current_node = self.head
      try:
        if current_node.next == None:
          self.head = current_node.next
          return ("Queue is empty.")
        else:
          self.head = current_node.next
          return self.head
      except AttributeError:
        return ("Queue is empty.")

    # Format list as a string
    def __str__(self):
        current_node = self.head
        qstring = ""
        if current_node is None:
          return("Queue is empty.")
        else:
          while current_node is not None:
            qstring += str(current_node.data)
            qstring += "-->"
            current_node = current_node.next
        qstring += "End"
        return qstring

# Test - create nodes and a linked list
q = Queue(Node("A"))
print("Queue contains: {}".format(q))
print("Type: {} \n".format(type(q)))

# Test - add item to the end of the list
print("Add the letter B.")
q.enqueue("B")
print("Queue contains: {}".format(q))

# Test - add item to the end of the list
print("\nAdd the letter C.")
q.enqueue("C")
print("Queue contains: {}".format(q))

# Test - remove item at the beginning of the list
print("\nRemove the item at the beginning of the list.")
q.dequeue()
print("Queue contains: {}".format(q))




"""
Your queue should start empty and support the following methods:
•	enqueue(item) adds the item to the back of the queue
•	dequeue() removes and returns the item at the front of the queue
•	peek() returns the front-most item, but does not remove it
•	isEmpty() returns true if the queue is empty
•	size() returns the number of items in the queue
"""