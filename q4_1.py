"""
Quiz 4.1
A palindrome is a word or a phrase that has the same characters
forwards and backwards. For example, "never odd or even", "racecar"
are palindromes.

Given a string containing a word or sequence of words,
write a function that determines if the string is a palindrome.
You can assume that there is no punctuation and all characters are lowercase.
"""

def pal_check(string):
    string = string.replace(" ", "").lower()

    if string == string[::-1]:
        return True
    else:
        return False

print('Is "Dianna" a palindrone?')
print(pal_check("Dianna"))

print('\nIs "Never odd or even" a palindrone?')
print(pal_check("never odd or even"))

print('\nIs "racecar" a palindrone?')
print(pal_check("racecar"))