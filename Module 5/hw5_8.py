"""
Homework 5.8
Now write a recursive function that does the same thing,
but it prints them in reverse order.
"""


def reverse_print_nums(nums):
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        print(nums[0])
    else:
        print(nums[-1])
        reverse_print_nums(nums[:-1])


numbers = [2, 4, 6, 8, 10]
print("List of numbers: {}".format(numbers))
reverse_print_nums(numbers)
