"""
Part 2 — Linked List
Another implementation of a list utilizes a linked list.
As discussed in class, a linked list is a series of nodes connected together.
A node contains some data and a pointer to the next node in the list.
The list’s last node points to null (None, nil, etc).
You’ll probably want to write a small Node class similar to what we did in class.
Submit file as HW2_2_Dianna_Tingg.py
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


# Create a linked list
class LinkedList:
    def __init__(self, head):
        self.head = head

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
            return print("Error. Index number out of range.")

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
            return print("Error. Index number out of range.")

    # Add value at end of list
    def add_to_end(self, new_node):
        current_index = 0
        current_node = self.head
        while current_node.next is not None:
            current_index += 1
            current_node = current_node.next
        current_node.next = new_node
        return self.head

    # Insert value anywhere in list
    def insert(self, new_node, index):
        current_index = 0
        current_node = self.head

        if index == 0:
            new_node.next = current_node
            self.head = new_node
        else:
            try:
                while current_index != (index - 1):
                    current_index += 1
                    current_node = current_node.next
                new_pointer = current_node.next
                current_node.next = new_node
                new_node.next = new_pointer
            except AttributeError:
                return print("Error. Index number out of range.")

        return self.head

    # Delete value anywhere in list
    def delete(self, delete_index):
        current_index = 0
        current_node = self.head

        if delete_index == 0:
            self.head = current_node.next
            return self.head

        try:
            while current_index != (delete_index - 1):
                current_index += 1
                current_node = current_node.next

            current_node.next = current_node.next.next
            return self.head
        except AttributeError:
            return print("Error. Index number out of range.")

    # Format list as a string
    def __str__(self):
        current_node = self.head
        llstring = ""
        while current_node is not None:
            llstring += str(current_node.data)
            llstring += "-->"
            current_node = current_node.next
        llstring += "END"
        return llstring


# Test - create nodes and a linked list
node_a = Node("A")
node_a.next = Node("B")
node_a.next.next = Node("C")
ll = LinkedList(node_a)
print("Linked list contains: {}".format(ll))
print(type(ll))

# Test - get a value at a specific index
print("Item at position 1 is: {}".format(ll.get(1)))

# Test - search for a value
print("Is C in the list?: {}".format(ll.search("C")))
print("Is D in the list?: {}".format(ll.search("D")))

# Test - change value at a specific location
print("Change the value at index 2 to D.")
ll.change("D", 2)
print(ll)

# Test - add item at the end of list
print("Add the letter E.")
ll.add_to_end(Node("E"))
print("New linked list contains: {}".format(ll))

# Test - insert item at a specific location
print("Add the letter C to index 2")
ll.insert(Node("C"), 2)
print("New linked list contains: {}".format(ll))

# Test - delete item at a specific location
print("Delete the value at index 0")
ll.delete(0)
print("New linked list contains: {}".format(ll))
