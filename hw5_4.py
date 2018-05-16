"""
Homework 5.4
Convert the following recursive function to be iterative.
Note that you can’t actually run this as you don’t know
what the code for node is (other than seeing it has a
left attribute). The idea is that you should be able to
understand its behaviour and convert it to an iterative
version directly.

def recurer(node):
  if node.left:
    return recurer(node.left)
  else:
    return node
"""


def iterative(node):
    while node.left is not None:
        node = node.left
    return node
