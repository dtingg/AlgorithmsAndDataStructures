"""
Homework 6
Question 2
A magic index of an array is defined to be the index i such that A[i] == i.
Given a sorted array of distinct integers, write a function to find a magic
index, if one exists, in the array. If a magic index does not exist, the
function should return -1. What is your function's efficiency? Can you make
it more efficient?
"""


def magic_index(nums):
    for x in range(len(nums)):
        if nums[x] == x:
            return nums[x]
    return -1


print(magic_index([0]))
print(magic_index([1, 2, 3]))
print(magic_index([-1, 0, 2, 4, 5, 6]))
print(magic_index([-1, 0, 1, 2, 4, 10]))
