"""
Quiz 6
Question 3
Implement a function compress that takes a string and performs basic compression
using the counts of repeated characters. For example, the string aabcccccaaa
would become a2b1c5a3. You can assume the string has only lowercase letters
and is called with a string length of at least one.
"""


def compress(s):
    result = ""
    x = 1
    counter = 1
    while x <= len(s):
        if x == len(s):
            result += s[x - 1]
            result += str(counter)
            break

        elif s[x] == s[x - 1]:
            counter += 1
            x += 1
        else:
            result += s[x - 1]
            result += str(counter)
            x += 1
            counter = 1

    print(result)


test = "aabcccccaaa"
compress(test)
