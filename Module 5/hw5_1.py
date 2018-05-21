"""
Homework 5.1
Recall the palindrome exercise from quiz 4:
A palindrome is a word or a phrase that has the same characters
forwards and backwards. For example, "never odd or even",
"racecar" are palindromes.
Given a string containing a word or sequence of words, write a
function that determines if the string is a palindrome. You can
assume that there is no punctuation and all characters are lowercase.
Implement a function is_palindrome(chars) that takes as input a list
of character strings. For example:
racecar = ['r', 'a', 'c', 'e', 'c', 'a', 'r']
should_be_true = is_palindrome(racecar)
"""


# Use recursion to see if a list of characters is a palindrome
def is_palindrome(chars):
    if len(chars) < 2:
        return True
    elif chars[0] != chars[-1]:
        return False
    else:
        is_palindrome(chars[1:-1])
    return True


print('Is "dianna" a palindrome?')
dianna = ["d", "i", "a", "n", "n", "a"]
print(is_palindrome(dianna))

print('\nIs "racecar" a palindrome?')
racecar = ["r", "a", "c", "e", "c", "a", "r"]
print(is_palindrome(racecar))
