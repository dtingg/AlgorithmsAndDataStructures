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
    def __init__(self):
        self.head = None

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

    # Add value at end of list
    def add_to_end(self, new_node):
        current_index = 0
        current_node = self.head

        if current_node is None:
            self.head = Node(new_node)
        else:
            while current_node.next is not None:
                current_index += 1
                current_node = current_node.next
            current_node.next = Node(new_node)
            return self.head

    # Insert value anywhere in list
    def insert(self, new_node, index):
        current_index = 0
        current_node = self.head

        if index == 0:
            new_node = Node(new_node)
            new_node.next = current_node
            self.head = new_node
        else:
            try:
                while current_index != (index - 1):
                    current_index += 1
                    current_node = current_node.next
                new_pointer = current_node.next
                new_node = Node(new_node)
                current_node.next = new_node
                new_node.next = new_pointer
            except (AttributeError, TypeError):
                return print("Error. Index not in range.")
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
        except (AttributeError, TypeError):
            return print("Error. Index not in range.")

    # Format list as a string
    def __str__(self):
        current_node = self.head
        llstring = ""
        if current_node is None:
            return "Empty"
        else:
            while current_node is not None:
                llstring += str(current_node.data)
                llstring += "-->"
                current_node = current_node.next
            llstring += "END"
            return llstring


# Test - create an empty linked list
ll = LinkedList()
print("Linked list contains: {}".format(ll))
print("Type: {} \n".format(type(ll)))

# Add the letter "A" to the list.
print('Add the letter "A" to the list.')
ll.add_to_end("A")
print(ll)

# Add the letter "B" to the list.
print('Add the letter "B" to the list.')
ll.add_to_end("B")
print(ll)

# Test - get a value at a specific index
print("\nItem at position 1 is: {}\n".format(ll.get(1)))

# Test - search for a value
print("Is A in the list?: {}".format(ll.search("A")))
print("Is D in the list?: {}\n".format(ll.search("D")))

# Test - change value at a specific location
print("Change the value at index 1 to D.")
ll.change("D", 1)
print("New linked list contains: {}\n".format(ll))

# Test - insert item at a specific location
print("Add the letter C to index 1")
ll.insert("C", 1)
print("New linked list contains: {}\n".format(ll))

# Test - delete item at a specific location
print("Delete the value at index 0")
ll.delete(0)
print("New linked list contains: {}".format(ll))
