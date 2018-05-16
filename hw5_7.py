"""
Homework 5.7
Write a recursive function that takes a list of integers
as input and prints each value, one per line, in order.
"""


def print_nums(nums):
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        print(nums[0])
    else:
        print(nums[0])
        print_nums(nums[1:])


numbers = [2, 4, 6, 8, 10]
print("List of numbers: {}".format(numbers))
print_nums(numbers)
