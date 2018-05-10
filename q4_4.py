"""
Quiz 4.4

An animal shelter, which holds only dogs and cats,
operates on a strictly first in, first out basis.
People must adopt either the oldest (based on arrival time)
of all animals at the shelter, or they can select whether
they would prefer a dog or a cat (and will receive the oldest
animal of that type). They cannot select which specific animal
they would like.

Create the data structures to maintain this system and implement
operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat.
Use an existing LinkedList implementation you may have.

You may assume any type of input that is convenient for your
programming language, as long as you can provide a name for the
animal and distinguish between dog and cat.
"""
import datetime


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
        value = self.head.data
        self.head = self.head.next
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


# Create a class for animal age
class AnimalAge:
    def __init__(self, name):
        self.name = name
        self.age = datetime.datetime.now()


# Create a class for shelter
class Shelter:
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()

# Add a pet.  Ask for name and type.
    def add_pet(self, name, type):
        if type is "cat":
            self.cats.enqueue(AnimalAge(name))
        elif type is "dog":
            self.dogs.enqueue(AnimalAge(name))
        else:
            return "Error. Animal must be a cat or a dog."

    # Adopt a cat - use the first one in the queue
    def adopt_cat(self):
        try:
            pet = self.cats.dequeue()
            print ("Congrats, you have adopted a cat named {}.".format(pet.name))
        except AttributeError:
            return print("There are no cats available.")
        return pet.name

    # Adopt a dog - use the first one in the queue
    def adopt_dog(self):
        try:
            pet = self.dogs.dequeue()
            print("Congrats, you have adopted a dog named {}.".format(pet.name))
        except AttributeError:
            return print("There are no dogs available.")
        return pet.name

    # Adopt any - compare the first one in the cat vs dog queues
    def adopt_any(self):
        dog_age = self.dogs.peek().age
        cat_age = self.cats.peek().age

        if dog_age < cat_age:
            return self.adopt_dog()
        else:
            return self.adopt_cat()

# Create a test class
test = Shelter()

# Add some dogs and cats
test.add_pet("Nicholas", "cat")
test.add_pet("Sam", "dog")
test.add_pet("Lion", "cat")
test.add_pet("Shasta", "dog")
test.add_pet("Fluffy", "cat")
test.add_pet("Mango", "dog")

# Adopt any pet
test.adopt_any()

# Adopt a dog
test.adopt_dog()

# Adopt a cat
test.adopt_cat()
