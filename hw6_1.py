"""
Homework 6
Question 1
Given an array of strings, write a function that returns an array
of the strings sorted by their length. If the length of any of the
strings are equal, they should be in the order they were in the
original array (i.e., the sort should be stable).
"""


def sorted_by_length(strings):
    d = {}
    for x in strings:
        d[x] = len(x)
    return sorted(d, key=d.get)


print(sorted_by_length(["melon", "apple", "kiwi", "orange", "banana"]))
print(sorted_by_length([]))
print(sorted_by_length(['ab', 'c']))
print(sorted_by_length(['b', 'a', 'two']))
print(sorted_by_length(['one', 'two', 'three', 'four']))
