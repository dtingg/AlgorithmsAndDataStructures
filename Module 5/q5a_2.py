"""
Quiz 5A
Question 2
Given a linked list, write a function, reverse_print(l),
that prints the values of each node of the list reverse
order. For example, calling the function with the list
1 -> 2 -> 3 would print:
3
2
1
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


# Create a Linked List
class LinkedList:
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
            return "List is empty."
        else:
            value = self.head.data
            self.head = current_node.next
        return value

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


# Create a function that prints the list in reverse order
def reverse_print(node):
    if node.next is None:
        print(node.data)
    else:
        reverse_print(node.next)
        print(node.data)


test = LinkedList()
test.enqueue("A")
test.enqueue("B")
test.enqueue("C")

reverse_print(test.head)
