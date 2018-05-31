"""
Homework 7

International Morse Code defines a standard encoding where each Latin letter is
mapped to a series of dots and dashes (the ISO Latin Alphabet contains the 26
letters you are familiar with).

Additionally, a period is .-.-.- and a comma is --..--. Morse Code is
case-insensitive, but for our purposes, use only lowercase letters.

For our purposes, a space character will be used to delineate letters and a /
character will be used to delineate words.

As an example, the sequence .... . .-.. .-.. --- --..-- / -.-. .-.. .- ...
... .-.-.- / - .... .. ... / .. ... / .- / - . ... - .-.-.- represents the
sentence "Hello, class. This is a test.". You can use Morse Code Translator
https://morsecode.scphillips.com/translator.html to play around with translating
to and from Morse.
"""
# Question 1 - For our first problem, write a function that converts a given word
# into Morse Code. Only a single word will be supplied but it may end in an optional
# punctuation character. For example, "Hello" and "Hello," are both valid inputs to
# this function.

morse_dict = {"": "", "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
              "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
              "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
              "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
              "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
              "z": "--..", ".": ".-.-.-", ",": "--..--", " ": "/"}


def encode_word(word):
    letters = []
    for x in word:
        letters.append(morse_dict[x])
    new_word = " ".join(letters)
    return new_word


print(encode_word(""))
print(encode_word("a"))
print(encode_word("is"))
print(encode_word("bananas"))
print(encode_word("period."))
print(encode_word("comma,"))


# Question 2 - Write a function that does the opposite of the previous one.
# That is, it decodes a Morse Code sequence into a word.


def decode_word(encoded_word):
    letters = encoded_word.split(" ")
    word = ""
    for x in letters:
        for k, v in morse_dict.items():
            if v == x:
                word += k
                break
    return word


print(decode_word(''))
print(decode_word('.-'))
print(decode_word('.. ...'))
print(decode_word('-... .- -. .- -. .- ...'))
print(decode_word('.--. . .-. .. --- -.. .-.-.-'))
print(decode_word('-.-. --- -- -- .- --..--'))

# Question 3 - Now that we're able to encode and decode words to Morse, we'd like
# to be able to convert entire sentences. Utilizing the previous function, write
# another function that decodes a Morse Code into a sequence of words.


def decode_words(encoded_words):
    letters = encoded_words.split(" ")
    word = ""
    for x in letters:
        for k, v in morse_dict.items():
            if v == x:
                word += k
                break
    return word


print(decode_words(''))
print(decode_words('--- -. .'))
print(decode_words('--- -. . .-.-.-'))
print(decode_words('--- -. . / - .-- ---'))
print(decode_words('--- -. . / - .-- --- .-.-.-'))
print(decode_words('--- -. . --..-- / - .-- --- --..-- / .- -. -.. / - .... .-. . . .-.-.-'))
print(decode_words('..-. .. .-. ... - .-.-.- / ... . -.-. --- -. -.. .-.-.- / - .... .. .-. -.. .-.-.-'))

# Question 4 - As before, we need the opposite version of the previous function,
# one that encodes words.


def encode_words(words):
    letters = []
    for x in words:
        letters.append(morse_dict[x])
    new_word = " ".join(letters)
    return new_word


print(encode_words(""))
print(encode_words("one"))
print(encode_words("one."))
print(encode_words("one two"))
print(encode_words("one two."))
print(encode_words("one, two, and three."))
print(encode_words("first. second. third."))
