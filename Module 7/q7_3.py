"""
Quiz 7
Question 3
Dupe Detection
Given a list of strings, determine which strings are repeated.
For example, in the list["kiwi", "apple", "banana", "orange", "banana", "kiwi"], the words kiwi and banana are repeated.
"""


def dupes(words):
    d = {}
    for x in words:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1

    duplicates = []
    for k, v in d.items():
        if v >= 2:
            duplicates.append(k)
    return duplicates


print(dupes(["kiwi", "apple", "banana", "orange", "banana", "kiwi"]))
