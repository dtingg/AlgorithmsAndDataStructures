"""
Quiz 5A
Question 3
Given an integer, we need to find the super
digit of the integer. We define super digit
of an integer x using the following rules:

If x has only 1 digit, then its super digit is x.
Otherwise, the super digit of x is equal to the
super digit of the digit-sum of x. Here, digit-sum
of a number is defined as the sum of its digits.

For example, the super digit of 9875 will be calculated as:

super_digit(9875) = super_digit(9+8+7+5)
                  = super_digit(29)
                  = super_digit(2+9)
                  = super_digit(11)
                  = super_digit(1+1)
                  = super_digit(2)
                  = 2.
Write the function super_digit(x).
"""


def super_digit(num):
    if num < 10:
        return num
    else:
        numlist = list(str(num))
        sub = 0
        for x in numlist:
            sub += int(x)
        return super_digit(sub)


print(super_digit(99))
