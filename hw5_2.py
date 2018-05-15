"""
Homework 5.2
Now, implement is_palindrome(string) from the previous question,
but instead of a list of characters as input, have your new
function take a string. For example:
should_be_true = is_palindrome("racecar")
You are not allowed to reverse the string. Use recursion.
Hint: you can use the function from the previous question
"""


# Use recursion to see if a string is a palindrone
def is_palindrone(string):
    if len(string) < 2:
        return True
    elif string[0] != string[-1]:
        return False
    else:
        is_palindrone(string[1:-1])
    return True


print('Is "dianna" a palindrone?')
print(is_palindrone("dianna"))

print('\nIs "racecar" a palindrone?')
print(is_palindrone("racecar"))
