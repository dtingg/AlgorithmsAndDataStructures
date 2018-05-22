"""
Quiz 6
Question 2
Given two sorted lists of integers, write a function merge that merges
the two lists and produces a new sorted list. Either input list can be empty.
For example:

A = [5, 10, 15, 20]
B = [3, 7, 13, 60]
C = merge(A, B)
# C now equals [3, 5, 7, 10, 13, 15, 20, 60]
"""


def merge_sort(l, m):
    result = []
    i = j = 0
    total = len(l) + len(m)
    while len(result) != total:
        if len(l) == i:
            result += m[j:]
            break
        elif len(m) == j:
            result += l[i:]
            break
        elif l[i] < m[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(m[j])
            j += 1
    return result


A = [5, 10, 15, 20]
B = [3, 7, 13, 60]
print(merge_sort(A, B))
