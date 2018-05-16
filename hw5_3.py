"""
Homework 5.3
In lecture, we wrote a function, sum(nums), that sums
all the numbers in the passed list. Modify the function
to support a list of lists. For example:
nested_nums = [[1, 2], [3, 4], [5]]
should_be_fifteen = sum(nested_nums)
"""


def sum_nested(nested_list):
    if not nested_list:
        return 0
    elif not isinstance(nested_list, (list)):
        return nested_list
    else:
        return sum_nested(nested_list[0]) + sum_nested(nested_list[1:])


numbers1 = [[1, 2], [3, 4], [5]]
print("Numbers: {}".format(numbers1))
print("The sum of this list is: {}".format(sum_nested(numbers1)))