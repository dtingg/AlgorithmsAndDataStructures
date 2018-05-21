"""
Homework 5.5
Convert this iterative function to be recursive. Same
idea as the previous question — think it through, maybe
use some paper and pencil, and convert it directly.

def iterer(n):
    x = 1
    while n > 1:
        x += 1
        n = n / 2
    return x
"""


def recurer(n):
    if n <= 1:
        return 1
    else:
        return 1 + recurer(n/2)
