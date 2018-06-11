"""
Homework 8
For this homework, you’ll be implementing a binary search tree.

The first problem requires you to write a function that creates a tree object given
a list of integers. The tree should be created by inserting the values of the list
in the order they appear in the list.

In order to automatically verify the structure of produced tree, problems two and
three have you produce in-order and pre-order representations of the tree.
"""


# 1. Write a function that takes in a list of integers, creates a binary search tree with
# those integers, and returns the tree.


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
        elif self.value < data:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)

    def inorder(self):
        numbers = []
        if self:
            if self.left:
                numbers += self.left.inorder()
            numbers.append(self.value)
            if self.right:
                numbers += self.right.inorder()
        return numbers

    def preorder(self):
        numbers = []
        if self:
            numbers.append(self.value)
            if self.left:
                numbers += self.left.preorder()
            if self.right:
                numbers += self.right.preorder()
        return numbers

    def height(self):
        if self.left and self.right:
            return 1 + max(self.left.height(), self.right.height())
        elif self.left:
            return 1 + self.left.height()
        elif self.right:
            return 1 + self.right.height()
        else:
            return 0

    def sum(self):
        if self.left and self.right:
            return self.left.sum() + self.right.sum() + self.value
        elif self.left:
            return self.left.sum() + self.value
        elif self.right:
            return self.right.sum() + self.value
        else:
            return self.value

    def search(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        else:
            if self.right:
                return self.right.search(data)
            else:
                return False


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)

    def height(self):
        if self.root:
            return self.root.height()
        else:
            return 0

    def sum(self):
        if self.root:
            return self.root.sum()
        else:
            return 0

    def search(self, data):
        if self.root:
            return self.root.search(data)
        else:
            return False


def create_tree(integers):
    tree = BinaryTree()
    for x in integers:
        tree.insert(x)
    return tree


# 2. Write a function that returns the in-order traversal of a given tree as
# space-separated string. For example, a tree created with the value list
# [10, 15, 7, 9, 3, 24] should produce the output 3 7 9 10 15 24.


def in_order(tree):
    numbers = tree.root.inorder()
    num_string = " ".join(str(x) for x in numbers)
    return num_string


# 3. Write a function that returns the pre-order traversal of a given tree as
# space-separated string. For example, a tree created with the value list
# [10, 15, 7, 9, 3, 24] should produce the output 10 7 3 9 15 24.


def pre_order(tree):
    numbers = tree.root.preorder()
    num_string = " ".join(str(x) for x in numbers)
    return num_string


# 4. Recall that the height of a tree is the length of the longest path from the
# root to a leaf. The blue example tree above would have a height of 2. A tree
# with only one node (the root node) would have a height of 0. Write a function
# that determines the height of a given tree.


def height(tree):
    return tree.root.height()


# 5. Write a function that returns the sum of all values in a tree.


def sum(tree):
    return tree.root.sum()


# 6. Write a function that returns a bool indicating that a value exists
# (or not) in a given tree.


def exists(tree, data):
    return tree.root.search(data)
