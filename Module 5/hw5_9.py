"""
Homework 5.9
Implement the recursive function reverse_list(l) that
takes a list as input and returns a _new_ list containing
the elements of l, but in reverse order. Remember that this
function should be recursive — no looping!
"""


def reverse_list(nums):
    if len(nums) < 2:
        return nums
    else:
        new_list = reverse_list(nums[1:])
        new_list.append(nums[0])
    return new_list


numbers = [2, 4, 6, 8]
print("Numbers: {}".format(numbers))
print("Reverse list: {}".format(reverse_list(numbers)))
