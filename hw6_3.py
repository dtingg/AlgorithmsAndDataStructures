"""
Homework 6
Question 3

Given an array of size n, write a function that finds the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times. 
You may assume that the array is non-empty and the majority element always exist in the array.
"""


def majority(nums):
    d = {}
    for x in nums:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1

    max_freq = max(d.values())

    for k, v in d.items():
        if v == max_freq:
            return k


print(majority([1]))
print(majority([0, 0, 1]))
print(majority([-5, 0, -5, 5, -5]))
print(majority([1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3]))
print(majority([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]))
