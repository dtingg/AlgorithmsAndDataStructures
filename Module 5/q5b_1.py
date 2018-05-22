"""
Quiz 5B
Question 1
Implement insertion sort. You may have it operate on any kind of
list implementation (node, array, etc) and can assume that the
list will contain only integers.
"""


def insertion_sort(nums):
    for index in range(1, len(nums)):
        value = nums[index]
        i = index - 1
        while i >= 0:
            if value < nums[i]:
                nums[i+1] = nums[i]
                nums[i] = value
                i -= 1
            else:
                break
    return nums


test = [5, 1, 3, 6]
print(insertion_sort(test))
