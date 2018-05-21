"""
Quiz 5A
Question 1
Write the function bit_combos(n) that prints all
possible combinations of 1 and 0 for n bits. For
example, if the function receives 2 as the number
of bits, it should print:
00
01
10
11
You cannot use any mathematical operators.
"""


def bit_combos(n):
    if n == 1:
        return ["0", "1"]
    else:
        new_combos = []
        for combo in bit_combos(n-1):
            new_combos.append("0" + combo)
            new_combos.append("1" + combo)
        return new_combos


print(bit_combos(4))
