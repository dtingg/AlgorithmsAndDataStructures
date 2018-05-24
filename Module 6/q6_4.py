"""
Quiz 6
Question 4
Implement Merge Sort
"""


# Merge two sorted lists into one sorted list
def merge(l, m):
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


# Sort one list of integers
def merge_sort(data):
    if len(data) < 2:
        return data
    else:
        midpoint = int(len(data)/2)
        left = merge_sort(data[:midpoint])
        right = merge_sort(data[midpoint:])
    return merge(left, right)


A = [5, 10, 15, 20]
B = [3, 7, 13, 60]
print(merge(A, B))

C = [27, 53, 7, 25, 33, 2, 32, 47, 43]
print(merge_sort(C))
