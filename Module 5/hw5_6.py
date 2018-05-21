"""
Homework 5.6
A child is running up a staircase with n steps and
can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a method, step_ways(n) to count how many
possible ways the child can run up _n_ stairs. For
example, step_ways(4)should return 7 since a child
can go up the stairs in the following combinations:
1 + 1 + 1 + 1
1 + 1 + 2
1 + 2 + 1
1 + 3
2 + 1 + 1
2 + 2
3 + 1
"""


def step_ways(n):
    if n == 1 or n == 0:
        return 1
    elif n == 2:
        return 2
    else:
        return step_ways(n-3) + step_ways(n-2) + step_ways(n-1)


test = 7
print("For {} stairs, there are {} combinations.".format(test, step_ways(test)))